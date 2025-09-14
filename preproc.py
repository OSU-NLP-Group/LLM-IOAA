from argparse import ArgumentParser
import json
import os
import re

FIGURES_SUBDIR = 'images'

def extract_figures(tex_content):
    pattern = r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}'
    return re.findall(pattern, tex_content)

def preprocess_tex_file(tex_path, figures_dir):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, flags=re.DOTALL)
    content = match.group(1) if match else content
    content = content.strip()

    figures = extract_figures(content)

    figures_paths = []
    for fig in figures:
        fig_fname = fig.split("/")[-1]
        fig_path = os.path.join(figures_dir, fig_fname)

        if not fig_path.endswith(".png"):
            fig_path += ".jpg"

        figures_paths.append(fig_path)

    return {
        'filename': tex_path,
        'problem': content,
        'figures': figures_paths
    }

def preprocess_data_folder(data_dir):
    results = []

    for root, _, files in os.walk(data_dir):
        for fname in files:
            if fname.endswith('.tex'):
                tex_path = os.path.join(root, fname)
                figures_dir = os.path.join(root, FIGURES_SUBDIR)
                result = preprocess_tex_file(tex_path, figures_dir)
                results.append(result)

    return results

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        "--data_dir",
        type=str,
        default="data/2025",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="ioaa_data.json",
    )

    args = parser.parse_args()

    processed = preprocess_data_folder(args.data_dir)
    with open(args.output_file, 'w', encoding='utf-8') as f:
        json.dump(processed, f, indent=2)