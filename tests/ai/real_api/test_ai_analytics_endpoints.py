import allure
import pytest

from utils.config import Config
from utils.api_client import APIClient


def assert_success_response(response):
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    return data


@allure.feature("Real Project GenAI QA")
@allure.story("General AI Ask API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_ask_general_prompt():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.ask_ai(
        "Write one short welcoming sentence for restaurant customers."
    )

    data = assert_success_response(response)

    assert "success" in data
    assert data["success"] is True

    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"].strip()) > 0


@allure.feature("Real Project GenAI QA")
@allure.story("AI Forecast API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_forecast_endpoint():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.get_ai_forecast()

    if response.status_code in [403, 404]:
        pytest.skip(f"Forecast endpoint not enabled in this environment: {response.text}")

    data = assert_success_response(response)

    assert len(data.keys()) > 0


@allure.feature("Real Project GenAI QA")
@allure.story("AI Inventory Predictions API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_inventory_predictions_endpoint():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.get_inventory_predictions()

    if response.status_code in [403, 404]:
        pytest.skip(
            f"Inventory predictions endpoint not enabled in this environment: {response.text}"
        )

    data = assert_success_response(response)

    assert len(data.keys()) > 0


@allure.feature("Real Project GenAI QA")
@allure.story("AI Price Intelligence API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_price_intelligence_endpoint():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.get_price_intelligence()

    if response.status_code in [403, 404]:
        pytest.skip(
            f"Price intelligence endpoint not enabled in this environment: {response.text}"
        )

    data = assert_success_response(response)

    assert len(data.keys()) > 0


@allure.feature("Real Project GenAI QA")
@allure.story("AI Profit Analysis API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_profit_analysis_endpoint():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.get_profit_analysis()

    if response.status_code in [403, 404]:
        pytest.skip(
            f"Profit analysis endpoint not enabled in this environment: {response.text}"
        )

    data = assert_success_response(response)

    assert len(data.keys()) > 0