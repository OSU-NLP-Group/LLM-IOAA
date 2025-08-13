from argparse import ArgumentParser
from litellm import completion

import os

class LiteLlmEngine():
    def __init__(self, model_name, model_args_dict):
        self.model_name = model_name
        self.vllm_server = None

        if self.model_name.startswith("hosted_vllm"):
            self.vllm_server = model_args_dict["vllm_server"]
        else:
            if self.model_name.startswith("bedrock"):
                os.environ["AWS_ACCESS_KEY_ID"] = model_args_dict["aws_access_key_id"]
                os.environ["AWS_SECRET_ACCESS_KEY"] = model_args_dict["aws_secret_access_key"]
                os.environ["AWS_REGION_NAME"] = model_args_dict["aws_region_name"]
            else:
                os.environ["OPENAI_API_KEY"] = model_args_dict["openai_api_key"]


    def respond(self, messages, temperature=1.0, top_p=1.0, max_tokens=16384):
        if self.model_name.startswith("bedrock"):
            responses = completion(
                model=self.model_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )
        elif self.model_name.startswith("hosted_vllm"):
            responses = completion(
                model=self.model_name,
                messages=messages,
                api_base=self.vllm_server,
                n=1,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )
        else:
            responses = completion(
                model=self.model_name,
                messages=messages,
                n=1,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
            )

        return {
            "responses": [o.message.content for o in responses.choices],
            "prompt_tokens": responses.usage.prompt_tokens, 
            "completion_tokens": responses.usage.completion_tokens,
        }


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

    args = parser.parse_args()
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

    prompt = """You are an expert in Astronomy and Astrophysics. Please think step by step and solve the given problem with a complete, detailed, and thorough answer. 
Please rigorously justify and clearly explain each step of your solution and do not skip important steps. A correct final answer with flawed or incomplete reasoning will receive no credit.
Please use LaTeX to format your answer.

Here is the problem statement:
A peculiar asteroid of mass, $m$, was spotted at a distance, $d$, from a star with mass, $M$. The magnitude of the asteroid's velocity at the time of the observation was $v = \\sqrt{\\frac{GM}{d}}$, where $G$ is the universal gravitational constant. The distance $d$ is much larger than the radius of the star.

For both of the following items, express your answers in terms of $M$, $d$, and physical or mathematical constants.

\\begin{parts}

    \\part[8] If the asteroid is initially moving exactly towards the star, how long will it take for it to collide with the star?

    \\part[2] If the asteroid is instead initially moving exactly away from the star, how long will it now take for it to collide with the star?

\\end{parts}"""

    print(engine.respond([{"role": "user", "content": prompt}]))