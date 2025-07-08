from openai import OpenAI
from app.core.config import config


class LLM(object):
    def __init__(self):
        self.client = OpenAI(
            api_key=config.llm_api_key, base_url="https://api.perplexity.ai"
        )

    def analysis(self):
        response = self.client.chat.completions.create(
            model="sonar",  # 可选模型，按需更换
            messages=[{"role": "user", "content": "你好，Perplexity！"}],
        )

        return response.model_dump()
