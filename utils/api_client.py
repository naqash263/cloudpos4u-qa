import requests
from utils.logger import get_logger


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.branch_id = None
        self.branch_code = None
        self.logger = get_logger(self.__class__.__name__)

    def login(self, email, password):
        self.logger.info("Sending login API request")

        response = requests.post(
            f"{self.base_url}/user/login",
            json={
                "email": email,
                "password": password
            }
        )

        self.logger.info(f"Login API response status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            self.token = data.get("accessToken")
            self.branch_id = data.get("data", {}).get("branchId")
            self.branch_code = data.get("data", {}).get("branch", {}).get("code")

        return response

    def get_headers(self):
        return {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}",
            "x-branch-id": self.branch_id,
            "x-branch-code": self.branch_code or "",
            "Content-Type": "application/json"
        }

    def get_cookies(self):
        return {
            "accessToken": self.token
        }

    def get_all_dishes(self):
        self.logger.info("Sending get all dishes API request")

        response = requests.get(
            f"{self.base_url}/dish/all",
            headers=self.get_headers(),
            cookies=self.get_cookies()
        )

        self.logger.info(f"Get all dishes API response status: {response.status_code}")

        return response

    def create_order(self, payload):
        self.logger.info("Sending create order API request")

        response = requests.post(
            f"{self.base_url}/order/",
            json=payload,
            headers=self.get_headers(),
            cookies=self.get_cookies()
        )

        self.logger.info(f"Create order API response status: {response.status_code}")

        return response