import requests
from utils.logger import get_logger


class BaseAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.token = None
        self.branch_id = None
        self.branch_code = None
        self.logger = get_logger(self.__class__.__name__)

    def get_headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}",
            "x-branch-id": self.branch_id or "",
            "x-branch-code": self.branch_code or "",
            "Content-Type": "application/json"
        }

    def get_cookies(self):
        return {
            "accessToken": self.token
        }

    def request(self, method, endpoint, json=None, headers=None, cookies=None, auth=True):
        url = f"{self.base_url}{endpoint}"

        final_headers = self.get_headers() if auth else {}
        final_cookies = self.get_cookies() if auth else {}

        if headers is not None:
            final_headers = headers

        if cookies is not None:
            final_cookies = cookies

        self.logger.info(f"Sending {method.upper()} request: {endpoint}")

        response = requests.request(
            method=method,
            url=url,
            json=json,
            headers=final_headers,
            cookies=final_cookies
        )

        self.logger.info(
            f"{method.upper()} {endpoint} response status: {response.status_code}"
        )

        if response.status_code >= 400:
            self.logger.info(f"Error response: {response.text}")

        return response