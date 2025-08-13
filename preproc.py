import json
import os
import re

DATA_DIR = 'data/'
FIGURES_SUBDIR = 'Figures'

def extract_figures(tex_content):
    # Matches \includegraphics[...]{filename}
    pattern = r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}'
    return re.findall(pattern, tex_content)

def preprocess_tex_file(tex_path, figures_dir):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\\', '\\\\')
    # print(content)
    figures = extract_figures(content)
    figures_paths = [os.path.join('data', fig) for fig in figures]
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
    processed = preprocess_data_folder(DATA_DIR)
    with open('ioaa_data.json', 'w', encoding='utf-8') as f:
        json.dump(processed, f, indent=2)