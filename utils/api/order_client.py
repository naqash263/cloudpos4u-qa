class OrderClient:
    def create_order(self, payload):
        return self.request(
            method="post",
            endpoint="/order/",
            json=payload
        )

    def create_order_with_custom_headers(self, payload, headers=None, cookies=None):
        return self.request(
            method="post",
            endpoint="/order/",
            json=payload,
            headers=headers or {},
            cookies=cookies or {},
            auth=False
        )