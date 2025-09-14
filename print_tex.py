import argparse
import json
import os
import re
import shutil
import subprocess

from litellm import cost_per_token


tex_imports = """\\documentclass{exam}
\\usepackage[utf8]{inputenc}
\\usepackage{amsthm}
\\usepackage{amssymb}
\\usepackage{mathrsfs}
\\usepackage{amsmath}
\\usepackage{mathtools}
\\usepackage{multirow}
\\usepackage{enumitem}
\\usepackage{mathabx}
\\usepackage{marginnote}
\\usepackage[version=3]{mhchem}
\\usepackage{float}
\\usepackage{hyperref}
\\usepackage{cleveref}
\\usepackage{xcolor} 
\\usepackage{cancel}
\\usepackage[per-mode=symbol]{siunitx}
\\usepackage{array}
\\usepackage{longtable}
\\usepackage{csquotes}
\\usepackage{mdwlist}
\\usepackage{indentfirst}
\\usepackage{caption}
\\usepackage{csquotes}
\\usepackage{lastpage}
\\usepackage{booktabs}
\\usepackage{tikz}
\\usepackage{pgfplots}
\\pgfplotsset{compat=1.17}
\\footer{}{\\thepage}{}
\\printanswers

"""


def read_jsonl(jsonl_path):
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield json.loads(line)


def extract_and_format_solution(response):
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', response, flags=re.DOTALL)
    content = match.group(1) if match else ""
    content = content.strip()

    solution = tex_imports + "\\begin{document}\n\n" + content + "\n\n\\end{document}"
    return solution


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add LLM response to TeX and generate PDFs.")
    parser.add_argument("--results_file", help="Path to the JSONL file with LLM outputs.")
    parser.add_argument("--model", help="LLM model used.")
    args = parser.parse_args()

    exp_name = args.results_file.split("/")[-1].replace(".jsonl", "")
    os.makedirs(f"results/tex/{exp_name}", exist_ok=True)

    costs = []
    for entry in read_jsonl(args.results_file):
        tex_path = entry["filename"]
        response = entry["response"]

        # Calculate cost using litellm
        prompt_tokens_cost_usd_dollar, completion_tokens_cost_usd_dollar = cost_per_token(
            model=args.model, 
            prompt_tokens=entry.get("prompt_tokens", 0), 
            completion_tokens=entry.get("completion_tokens", 0)
        )
        cost = prompt_tokens_cost_usd_dollar + completion_tokens_cost_usd_dollar
        costs.append(cost)

        base_name = tex_path[5:].replace("/", "_").replace("\\", "_").replace(".tex", "")
        output_tex = os.path.join(f"results/tex/{exp_name}", f"{base_name}_solution.tex")

        try:
            new_tex = extract_and_format_solution(response)
            with open(output_tex, 'w', encoding='utf-8') as f:
                f.write(new_tex)
            print(f"Generated {output_tex} | Cost: ${cost:.6f}")
        except Exception as e:
            print(f"Error processing {tex_path}: {e}")

    avg_cost = sum(costs) / len(costs)
    print(f"\nTotal cost: ${sum(costs):.6f}")
    print(f"Average cost per entry: ${avg_cost:.6f}")