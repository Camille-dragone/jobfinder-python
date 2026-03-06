import os
from langchain_openai import ChatOpenAI

def get_llm_abstraction():
    api_key = os.getenv("OVH_AI_ENDPOINTS_ACCESS_TOKEN")
    if not api_key:
        raise Exception("OVH_AI_ENDPOINTS_ACCESS_TOKEN is not set")

    return ChatOpenAI(
        model="Mistral-7B-Instruct-v0.3",
        api_key=api_key,
        base_url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1",
        temperature=0,
    )
