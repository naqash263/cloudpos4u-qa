from utils.api.base_client import BaseAPIClient
from utils.api.auth_client import AuthClient
from utils.api.menu_client import MenuClient
from utils.api.order_client import OrderClient
from utils.api.ai_client import AIClient


class APIClient(
    BaseAPIClient,
    AuthClient,
    MenuClient,
    OrderClient,
    AIClient
):
    pass