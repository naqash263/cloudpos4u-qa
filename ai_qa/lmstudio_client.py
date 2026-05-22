import os
from openai import OpenAI


class LMStudioClient:
    def __init__(self):
        self.base_url = os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1")
        self.model = os.getenv("LM_STUDIO_MODEL", "local-model")

        self.client = OpenAI(
            base_url=self.base_url,
            api_key="lm-studio"
        )

    def chat(self, prompt, temperature=0.1, max_tokens=1000):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI order extraction assistant for a restaurant POS system. "
                        "Return only valid JSON. Do not include explanation or markdown."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content