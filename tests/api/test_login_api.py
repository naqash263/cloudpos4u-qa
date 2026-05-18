from utils.config import Config
from utils.api_client import APIClient


def test_login_api_success():
    api = APIClient(Config.API_BASE_URL)

    response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "User login successfully!"
    assert "accessToken" in data
    assert data["data"]["email"] == Config.ADMIN_EMAIL
    assert data["data"]["role"] == "Admin"
    assert data["data"]["status"] == "Active"


def test_login_api_invalid_password():
    api = APIClient(Config.API_BASE_URL)

    response = api.login(
        Config.ADMIN_EMAIL,
        "WrongPassword123!"
    )

    assert response.status_code == 401

    data = response.json()

    assert data["status"] == 401
    assert data["message"] == "Invalid Credentials"
    assert "accessToken" not in data