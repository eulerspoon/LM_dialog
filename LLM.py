import openai
import os

class LLM:
    def __init__(self, model_title):
        self.model_title = model_title

        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("OPENAI_BASE_URL")

        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def answer(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_title,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content