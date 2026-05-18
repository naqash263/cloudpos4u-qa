import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None
        self.branch_id = None
        self.branch_code = None

    def login(self, email, password):
        response = requests.post(
            f"{self.base_url}/user/login",
            json={
                "email": email,
                "password": password
            }
        )

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
        return requests.get(
            f"{self.base_url}/dish/all",
            headers=self.get_headers(),
            cookies=self.get_cookies()
        )

    def create_order(self, payload):
        return requests.post(
            f"{self.base_url}/order/",
            json=payload,
            headers=self.get_headers(),
            cookies=self.get_cookies()
        )