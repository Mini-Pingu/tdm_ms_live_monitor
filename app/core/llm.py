from openai import OpenAI
from app.core.config import config


class LLM(object):
    def __init__(self):
        self.client = OpenAI(
            api_key=config.llm_api_key, base_url="https://api.perplexity.ai"
        )

    def analysis(self, model: str = "sonar", text: str = "", prompt: str = ""):
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"{text} ||| {prompt}"}],
        )

        return response.choices[0].message.content


llm_handler = LLM()
