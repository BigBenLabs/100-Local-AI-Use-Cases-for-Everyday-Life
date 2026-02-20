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