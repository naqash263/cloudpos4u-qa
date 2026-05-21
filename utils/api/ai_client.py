class AIClient:

    def ask_staff_ai(self, prompt, mode="general", language="English", history=None):
        payload = {
            "prompt": prompt,
            "branchId": self.branch_id,
            "mode": mode,
            "language": language,
            "history": history or []
        }

        return self.request(
            method="post",
            endpoint="/ai/ask-staff",
            json=payload
        )

    def ask_staff_ai_with_custom_headers(self, payload, headers=None, cookies=None):
        return self.request(
            method="post",
            endpoint="/ai/ask-staff",
            json=payload,
            headers=headers or {},
            cookies=cookies or {},
            auth=False
        )

    def ask_ai(self, prompt):
        payload = {
            "prompt": prompt
        }

        return self.request(
            method="post",
            endpoint="/ai/ask",
            json=payload
        )

    def test_ai_provider(self, provider="", api_key="", model=""):
        payload = {
            "provider": provider,
            "apiKey": api_key,
            "model": model
        }

        return self.request(
            method="post",
            endpoint="/ai/test",
            json=payload
        )

    def test_embedding_provider(
        self,
        openai_api_key="",
        embedding_model="text-embedding-3-small"
    ):
        payload = {
            "openAiApiKey": openai_api_key,
            "embeddingModel": embedding_model
        }

        return self.request(
            method="post",
            endpoint="/ai/test-embedding",
            json=payload
        )

    def get_ai_forecast(self):
        return self.request(
            method="get",
            endpoint="/ai/forecast"
        )

    def get_inventory_predictions(self):
        return self.request(
            method="get",
            endpoint="/ai/inventory-predictions"
        )

    def get_price_intelligence(self):
        return self.request(
            method="get",
            endpoint="/ai/price-intelligence"
        )

    def get_profit_analysis(self):
        return self.request(
            method="get",
            endpoint="/ai/profit-analysis"
        )