from utils.api.base_client import BaseClient


class MenuClient(BaseClient):
    def get_all_dishes(self):
        self.logger.info("Sending get all dishes API request")
        return self.get("/dish/all")

    def get_all_dishes_with_custom_headers(self, headers=None, cookies=None):
        self.logger.info("Sending get all dishes API request with custom headers")
        return self.get(
            "/dish/all",
            headers=headers or {},
            cookies=cookies or {}
        )