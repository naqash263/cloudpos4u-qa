from utils.api.auth_client import AuthClient
from utils.api.menu_client import MenuClient
from utils.api.order_client import OrderClient


class CloudPOSAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

        self.auth = AuthClient(base_url)
        self.menu = MenuClient(base_url)
        self.order = OrderClient(base_url)

        self.token = None
        self.branch_id = None
        self.branch_code = None

    def _sync_auth_context(self):
        self.token = self.auth.token
        self.branch_id = self.auth.branch_id
        self.branch_code = self.auth.branch_code

        self.menu.set_auth_context(
            token=self.token,
            branch_id=self.branch_id,
            branch_code=self.branch_code
        )

        self.order.set_auth_context(
            token=self.token,
            branch_id=self.branch_id,
            branch_code=self.branch_code
        )

    def clear_auth_context(self):
        self.token = None
        self.branch_id = None
        self.branch_code = None

        self.auth.clear_auth_context()
        self.menu.clear_auth_context()
        self.order.clear_auth_context()

    def login(self, email, password):
        response = self.auth.login(email, password)
        self._sync_auth_context()
        return response

    def get_all_dishes(self):
        return self.menu.get_all_dishes()

    def get_all_dishes_with_custom_headers(self, headers=None, cookies=None):
        return self.menu.get_all_dishes_with_custom_headers(
            headers=headers,
            cookies=cookies
        )

    def create_order(self, payload):
        return self.order.create_order(payload)

    def create_order_with_custom_headers(self, payload, headers=None, cookies=None):
        return self.order.create_order_with_custom_headers(
            payload=payload,
            headers=headers,
            cookies=cookies
        )

    def get_endpoint(self, endpoint):
        return self.menu.get(endpoint)