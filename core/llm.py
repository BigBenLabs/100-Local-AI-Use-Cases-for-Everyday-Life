# --- 1. Configuration area: Switch platforms here ---
# Optional values: 'lm_studio', 'nvidia', 'deepseek', 'zhipu'
# PROVIDER = 'lm_studio'

# LLM = {
#     "lm_studio": {
#         "base_url": "http://localhost:1234/v1",
#         "api_key": "lm-studio", 
#         "model": "qwen/qwen3-next-80b"
#     },
#     "nvidia": {
#         "base_url": "https://integrate.api.nvidia.com/v1",
#         "api_key": "Your NVIDIA_API_KEY",
#         "model": "meta/llama-3.1-405b-instruct" 
#     },
#     "deepseek": {
#         "base_url": "https://api.deepseek.com",
#         "api_key": "Your DEEPSEEK_API_KEY",
#         "model": "deepseek-chat"
#     },
#     "zhipu": {
#         "base_url": "https://open.bigmodel.cn/api/paas/v4",
#         "api_key": "Your GLM_API_KEY",
#         "model": "glm-4"
#     }
# }

# selected = LLM[PROVIDER]

# model = ChatOpenAI(
#     model=selected["model"],
#     api_key=selected["api_key"],
#     base_url=selected["base_url"],
#     temperature=0.1 # CFA 术语解释建议低随机性
# ).with_structured_output(FomatOutPut)

from langchain_openai import ChatOpenAI  # 需要安装: pip install langchain-openai

def get_model(provide="lmstudio",model_name="qwen/qwen3-next-80b",api_key="lm-studio"):

    LLM = {
        "lmstudio": {
            "base_url":"http://localhost:1234/v1"
        },
        "nvidia":{
            "base_url":"https://integrate.api.nvidia.com/v1"
        },
        "deepseek":{
            "base_url":"https://api.deepseek.com"
        },
        "zhipu":{
            "base_url": "https://open.bigmodel.cn/api/paas/v4",
        }
    }

    return ChatOpenAI(
        model=model_name,
        openai_api_key=api_key, 
        openai_api_base=LLM[provide]["base_url"],
        temperature=0.1
    )