from utils.api.base_client import BaseClient


class OrderClient(BaseClient):
    def create_order(self, payload):
        self.logger.info("Sending create order API request")
        return self.post("/order/", payload=payload)

    def create_order_with_custom_headers(self, payload, headers=None, cookies=None):
        self.logger.info("Sending create order API request with custom headers")
        return self.post(
            "/order/",
            payload=payload,
            headers=headers or {},
            cookies=cookies or {}
        )