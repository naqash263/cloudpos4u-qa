import requests


class LMStudioClient:
    def __init__(
        self,
        base_url="http://localhost:1234/v1",
        model="google/gemma-4-e4b",
        timeout=60
    ):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def chat(self, prompt):
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer lm-studio"
            },
            json={
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0,
                "max_tokens": 800
            },
            timeout=self.timeout
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]