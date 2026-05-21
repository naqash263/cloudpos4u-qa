import allure
import pytest
from utils.config import Config
from utils.api_client import APIClient

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("API Authentication")
@allure.story("Login API Success")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_api_success():
    api = APIClient(Config.API_BASE_URL)

    with allure.step("Send valid login API request"):
        response = api.login(
            Config.ADMIN_EMAIL,
            Config.ADMIN_PASSWORD
        )

    with allure.step("Validate login API response"):
        assert response.status_code == 200

        data = response.json()

        assert data["success"] is True
        assert data["message"] == "User login successfully!"
        assert "accessToken" in data
        assert data["data"]["email"] == Config.ADMIN_EMAIL
        assert data["data"]["role"] == "Admin"
        assert data["data"]["status"] == "Active"

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("API Authentication")
@allure.story("Login API Invalid Password")
@allure.severity(allure.severity_level.NORMAL)
def test_login_api_invalid_password():
    api = APIClient(Config.API_BASE_URL)

    with allure.step("Send login API request with invalid password"):
        response = api.login(
            Config.ADMIN_EMAIL,
            "WrongPassword123!"
        )

    with allure.step("Validate invalid credentials response"):
        assert response.status_code == 401

        data = response.json()

        assert data["status"] == 401
        assert data["message"] == "Invalid Credentials"
        assert "accessToken" not in data