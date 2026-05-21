import allure
import pytest

from tests.helpers.api_assertions import assert_success_response


@allure.feature("Real Project GenAI QA")
@allure.story("General AI Ask API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_ask_general_prompt(authenticated_ai_api_client):
    response = authenticated_ai_api_client.ask_ai(
        "Write one short welcoming sentence for restaurant customers."
    )

    if response.status_code in [403, 404]:
        pytest.skip(f"AI ask endpoint not enabled in this environment: {response.text}")

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
def test_ai_forecast_endpoint(authenticated_ai_api_client):
    response = authenticated_ai_api_client.get_ai_forecast()

    if response.status_code in [403, 404]:
        pytest.skip(f"Forecast endpoint not enabled in this environment: {response.text}")

    data = assert_success_response(response)

    assert len(data.keys()) > 0


@allure.feature("Real Project GenAI QA")
@allure.story("AI Inventory Predictions API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_inventory_predictions_endpoint(authenticated_ai_api_client):
    response = authenticated_ai_api_client.get_inventory_predictions()

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
def test_ai_price_intelligence_endpoint(authenticated_ai_api_client):
    response = authenticated_ai_api_client.get_price_intelligence()

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
def test_ai_profit_analysis_endpoint(authenticated_ai_api_client):
    response = authenticated_ai_api_client.get_profit_analysis()

    if response.status_code in [403, 404]:
        pytest.skip(
            f"Profit analysis endpoint not enabled in this environment: {response.text}"
        )

    data = assert_success_response(response)

    assert len(data.keys()) > 0