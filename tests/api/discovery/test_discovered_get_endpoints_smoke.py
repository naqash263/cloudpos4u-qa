import json
from pathlib import Path

import pytest
import allure

from utils.config import Config
from utils.api.cloudpos_api_client import CloudPOSAPIClient


ENDPOINTS_FILE = Path("tests/data/discovered_api_smoke_endpoints.json")


def load_discovered_get_endpoints():
    with open(ENDPOINTS_FILE, "r", encoding="utf-8") as file:
        endpoints = json.load(file)

    return [
        endpoint for endpoint in endpoints
        if endpoint["method"].upper() == "GET"
    ]


@pytest.fixture(scope="module")
def authenticated_api_client():
    api = CloudPOSAPIClient(Config.API_BASE_URL)

    response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert response.status_code == 200
    assert api.token is not None
    assert api.branch_id is not None

    return api


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Discovery API Smoke Tests")
@allure.story("Discovered GET Endpoints Respond Successfully")
@pytest.mark.parametrize("endpoint_config", load_discovered_get_endpoints())
def test_discovered_get_endpoint_returns_expected_status(
    authenticated_api_client,
    endpoint_config
):
    endpoint = endpoint_config["endpoint"]
    expected_status = endpoint_config.get("expected_status", 200)

    with allure.step(f"Call discovered GET endpoint: {endpoint}"):
        response = authenticated_api_client.get_endpoint(endpoint)

    with allure.step("Validate response status code"):
        assert response.status_code == expected_status

    with allure.step("Validate response is JSON"):
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type

    with allure.step("Validate response body is not empty"):
        assert response.text.strip() != ""