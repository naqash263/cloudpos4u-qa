from utils.api.base_client import BaseClient


class AuthClient(BaseClient):
    def login(self, email, password):
        self.logger.info("Sending login API request")

        response = self.post(
            "/user/login",
            payload={
                "email": email,
                "password": password
            },
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            },
            cookies={}
        )

        self.logger.info(f"Login API response status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()

            self.set_auth_context(
                token=data.get("accessToken"),
                branch_id=data.get("data", {}).get("branchId"),
                branch_code=data.get("data", {}).get("branch", {}).get("code")
            )

        return response