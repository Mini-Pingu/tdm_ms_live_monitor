import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("API_KEY", "123")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.perplexity.ai"
)

response = client.chat.completions.create(
    model="sonar",  # 可选模型，按需更换
    messages=[
        {"role": "user", "content": "你好，Perplexity！"}
    ]
)

response_dict = response.model_dump()
print(json.dumps(response_dict, indent=2, ensure_ascii=False))
