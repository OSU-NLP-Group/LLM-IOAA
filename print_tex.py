import argparse
import json
import os
import shutil
import subprocess


tex_imports = """
\\documentclass{exam}
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
\\footer{}{\\thepage}{}
\\printanswers

"""


def read_jsonl(jsonl_path):
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield json.loads(line)

def create_tex(tex_path, response):
    with open(tex_path, 'r', encoding='utf-8') as f:
        tex_content = f.read()

    new_content = (
        tex_imports +
        "\\begin{document}\n\n" +
        tex_content +
        "\n\n% LLM Response\n" +
        response +
        "\n\n\\end{document}"
    )

    return new_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add LLM response to TeX and generate PDFs.")
    parser.add_argument("--results_file", help="Path to the JSONL file with LLM outputs.")
    args = parser.parse_args()

    os.makedirs("results/tex", exist_ok=True)

    for entry in read_jsonl(args.results_file):
        tex_path = entry["filename"]
        response = entry["response"]
        
        base_name = tex_path[5:].replace("/", "_").replace("\\", "_").replace(".tex", "")
        exp_name = args.results_file.split("/")[-1].replace(".jsonl", "")
        output_tex = os.path.join("results/tex", f"{base_name}_{exp_name}.tex")

        try:
            new_tex = create_tex(tex_path, response)
            with open(output_tex, 'w', encoding='utf-8') as f:
                f.write(new_tex)
            print(f"Generated {output_tex}")
        except Exception as e:
            print(f"Error processing {tex_path}: {e}")