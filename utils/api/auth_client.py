class AuthClient:
    def login(self, email, password):
        payload = {
            "email": email,
            "password": password
        }

        response = self.request(
            method="post",
            endpoint="/user/login",
            json=payload,
            auth=False
        )

        if response.status_code == 200:
            data = response.json()
            self.token = data.get("accessToken")
            self.branch_id = data.get("data", {}).get("branchId")
            self.branch_code = data.get("data", {}).get("branch", {}).get("code")

        return response