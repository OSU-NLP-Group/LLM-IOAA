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
            elif self.model_name.startswith("azure"):
                os.environ["AZURE_API_KEY"] = model_args_dict["azure_api_key"]
                os.environ["AZURE_API_BASE"] = model_args_dict["azure_api_base"]
                os.environ["AZURE_API_VERSION"] = model_args_dict["azure_api_version"]
            else:
                os.environ["OPENAI_API_KEY"] = model_args_dict["openai_api_key"]


    def respond(self, messages, temperature=1.0, reasoning_effort="medium", max_tokens=64000):
        responses = completion(
            model=self.model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            reasoning_effort=reasoning_effort,
            timeout=900,
            max_retries=0,
        )

        return {
            "response": responses.choices[0].message.content, 
            "prompt_tokens": responses.usage.prompt_tokens, 
            "completion_tokens": responses.usage.completion_tokens,
        }
