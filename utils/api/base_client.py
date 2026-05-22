import requests
from utils.logger import get_logger


class BaseClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.logger = get_logger(self.__class__.__name__)
        self.token = None
        self.branch_id = None
        self.branch_code = None



    def set_auth_context(self, token=None, branch_id=None, branch_code=None):
        self.token = token
        self.branch_id = branch_id
        self.branch_code = branch_code

    def clear_auth_context(self):
        self.token = None
        self.branch_id = None
        self.branch_code = None

    def get_headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}" if self.token else "",
            "x-branch-id": self.branch_id or "",
            "x-branch-code": self.branch_code or "",
            "Content-Type": "application/json",
        }

    def get_cookies(self):
        return {
            "accessToken": self.token
        } if self.token else {}

    def get(self, endpoint, headers=None, cookies=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET request: {url}")

        response = requests.get(
            url,
            headers=headers if headers is not None else self.get_headers(),
            cookies=cookies if cookies is not None else self.get_cookies()
        )

        self.logger.info(f"GET response status: {response.status_code}")
        return response

    def post(self, endpoint, payload=None, headers=None, cookies=None):
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST request: {url}")

        response = requests.post(
            url,
            json=payload,
            headers=headers if headers is not None else self.get_headers(),
            cookies=cookies if cookies is not None else self.get_cookies()
        )

        self.logger.info(f"POST response status: {response.status_code}")
        return response