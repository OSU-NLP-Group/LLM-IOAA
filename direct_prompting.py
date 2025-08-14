from llm_engines.lite_llm import LiteLlmEngine

from argparse import ArgumentParser
from tqdm import tqdm

import asyncio
import base64
import json
import os


file_lock = asyncio.Lock()
sem = asyncio.Semaphore(4)


async def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


async def infer_one_example(example, engine, args, f_handle):
    if len(example['figures']) > 0:
        messages = [
            {"role": "user", "content": [{"type": "text", "text": example['instruction']}]}
        ]

        for fig in example['figures']:
            fig_data = await encode_image(fig)
            messages[0]["content"].append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{fig_data}"}
            })
    else:
        messages = [
            {"role": "user", "content": example['instruction']}
        ]

    responses = await asyncio.to_thread(
        engine.respond,
        messages,
        args.temperature,
        args.top_p,
        args.max_tokens
    )

    example_out = example.copy()
    example_out['response'] = responses['response']
    example_out['prompt_tokens'] = responses['prompt_tokens']
    example_out['completion_tokens'] = responses['completion_tokens']

    line = json.dumps(example_out, ensure_ascii=False)
    async with file_lock:
        f_handle.write(line + "\n")
        f_handle.flush()
        os.fsync(f_handle.fileno())


async def infer_w_sem(example, engine, args, f, pbar):
    async with sem:
        await infer_one_example(example, engine, args, f)
        pbar.update(1)


async def main(data, engine, args):
    tasks = []
    with open(args.output_file, "a", encoding="utf-8") as f, tqdm(total=len(data)) as pbar:
        for example in data:
            tasks.append(asyncio.create_task(infer_w_sem(example, engine, args, f, pbar)))

        await asyncio.gather(*tasks)


def load_completed_filenames(path: str) -> set:
    """
    Read an existing JSONL file and return the set of `filename` values
    already completed. Robust to blank/corrupt lines.
    """
    done = set()
    if not os.path.exists(path):
        return done
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                fn = obj.get("filename")
                if fn:
                    done.add(fn)
            except Exception:
                # Skip malformed lines; do not crash resume.
                continue
    return done


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--model_name",
        type=str,
        default="gpt-5-mini-2025-08-07",
    )
    parser.add_argument(
        "--aws_access_key_id",
        type=str,
        default="",
    )
    parser.add_argument(
        "--aws_secret_access_key",
        type=str,
        default="",
    )
    parser.add_argument(
        "--aws_region_name",
        type=str,
        default="",
    )
    parser.add_argument(
        "--openai_api_key",
        type=str,
        default="",
    )
    parser.add_argument(
        "--vllm_server",
        type=str,
        default="",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
    )
    parser.add_argument(
        "--top_p",
        type=float,
        default=1.0,
    )
    parser.add_argument(
        "--max_tokens",
        type=int,
        default=32768,
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="results/gpt5_mini_direct_prompting.jsonl",
    )

    args = parser.parse_args()

    with open('ioaa_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    completed = load_completed_filenames(args.output_file)
    data = [ex for ex in data if ex['filename'] not in completed]

    if len(completed) > 0:
        print(f"Resuming from {args.output_file}, skipping {len(completed)} completed examples.")
    
    engine = LiteLlmEngine(
        model_name=args.model_name,
        model_args_dict={
            "aws_access_key_id": args.aws_access_key_id,
            "aws_secret_access_key": args.aws_secret_access_key,
            "aws_region_name": args.aws_region_name,
            "openai_api_key": args.openai_api_key,
            "vllm_server": args.vllm_server
        }
    )

    asyncio.run(main(data, engine, args))