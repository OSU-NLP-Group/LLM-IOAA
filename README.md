# LLM-IOAA

Code and data for the paper "[Large Language Models Achieve Gold Medal Performance at the International Olympiad on Astronomy \& Astrophysics (IOAA)](https://arxiv.org/abs/2510.05016)".

## Updates:
- 2025/10/07: Data, prompts, and code released.

## Table of Contents
- [Environment Setup](#environment-setup)
- [Solution Generation with LLMs](#solution-generation-with-llms)
- [Contact](#contact)
- [Licensing Information](#licensing-information)
- [Disclaimer](#disclaimer)
- [Citation](#citation) 

## Environment Setup

To start, please create a conda environment and install the necessary packages as follows:
```
conda create -n llm-ioaa python=3.12
conda activate llm-ioaa
pip install -r requirements.txt
```

## Solution Generation with LLMs

### 1. Preprocesssing Exam Problems
You can use the following command to preprocess the provided data:
```
python -u preproc.py \
  --data_dir data/2025 \
  --output_file ioaa_data.json
```
**Arguments**
* **`--data_dir`** *(str)*
  Path to the directory containing the exam problems. If you are using our provided data, you can use `data/{exam_year}`, where `exam_year` is 2022, 2023, 2024, or 2025.
* **`--output_file`** *(str)*
  Path to save the JSON file containing processed data. If you are running the following steps using our code, you don't need to change anything for this argument.

### 2. Prompting LLMs to Solve Problems
You can run the LLMs with the following commands for different APIs:

**(1) OpenAI**
```
python -u direct_prompting.py \
  --model_name gpt-5-2025-08-07 \
  --openai_api_key $OPENAI_API_KEY \
  --output_file results/openai_outputs.jsonl
```

**(2) AWS Bedrock**
```
python -u direct_prompting.py \
  --model_name bedrock/us.anthropic.claude-opus-4-1-20250805-v1:0 \
  --aws_access_key_id $AWS_ACCESS_KEY_ID \
  --aws_secret_access_key $AWS_SECRET_ACCESS_KEY \
  --aws_region_name us-west-2 \
  --output_file results/aws_outputs.jsonl
```

**Arguments**
* **`--model_name`** *(str)*
  The model to use for direct prompting. Supports OpenAI or AWS-hosted models depending on the credentials provided.

* **`--aws_access_key_id`**, **`--aws_secret_access_key`**, **`--aws_region_name`** *(str, default: empty)*
  AWS credentials and region for running models on Amazon Bedrock or related AWS services.

* **`--openai_api_key`** *(str, default: empty)*
  API key for OpenAI models.

* **`--temperature`** *(float, default: `1.0`)*
  Sampling temperature. 

* **`--reasoning_effort`** *(str, default: `medium`)*
  Controls the amount of reasoning effort for models that support reasoning tokens. Options typically include `"low"`, `"medium"`, `"high"`.

* **`--max_tokens`** *(int, default: `64000`)*
  Maximum number of tokens to generate in a single completion.

* **`--output_file`** *(str)*
  Path to save the JSONL file containing model outputs.


### 3. Extracting Solution as TeX Files
You can run the the following commands to extract the TeX solutions and compile locally into PDFs:
```
python -u print_tex.py \
  --results_file results/model_outputs.jsonl \
  --model gpt-5-2025-08-07
```

**Arguments**
* **`--results_file`** *(str)*
  Path to save the JSONL file containing model outputs in the previous step.
* **`--model_name`** *(str)*
  The model to use in the previous step to calculate API cost (in USD).

## Contact

[Lucas Carrit Delgado Pinheiro](mailto:carritdelgadopinheiro.1@osu.edu), [Ziru Chen](mailto:chen.8336@osu.edu), [Yuan-Sen Ting](mailto:ting.74@osu.edu), and [Huan Sun](mailto:sun.397@osu.edu), The Ohio State University

## Licensing Information
All data and code under this repo is licensed under MIT License.

## Disclaimer

Our benchmark is constructed by converting the IOAA problems into LaTeX files. All past exams used this study are publicly available on the official IOAA website (https://ioaastrophysics.org/resources/problems-from-past-ioaa). We have consulted with members of the IOAA Executive Committee for their approval to use these exams in our study and release the files publicly in this repository.

## Citation

If you find our code and data useful, please cite our paper:

```
@misc{pinheiro2025largelanguagemodelsachieve,
      title={Large Language Models Achieve Gold Medal Performance at International Astronomy & Astrophysics Olympiad}, 
      author={Lucas Carrit Delgado Pinheiro and Ziru Chen and Bruno Caixeta Piazza and Ness Shroff and Yingbin Liang and Yuan-Sen Ting and Huan Sun},
      year={2025},
      eprint={2510.05016},
      archivePrefix={arXiv},
      primaryClass={astro-ph.IM},
      url={https://arxiv.org/abs/2510.05016}, 
}
```