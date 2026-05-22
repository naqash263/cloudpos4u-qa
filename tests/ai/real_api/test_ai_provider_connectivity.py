import allure
import pytest

from utils.config import Config
from utils.api.cloudpos_api_client import CloudPOSAPIClient


@allure.feature("Real Project GenAI QA")
@allure.story("AI Provider Connectivity")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_provider_connectivity():
    if not Config.AI_TEST_PROVIDER:
        pytest.skip("AI_TEST_PROVIDER is not configured")

    api = CloudPOSAPIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.test_ai_provider(
        provider=Config.AI_TEST_PROVIDER,
        api_key=Config.AI_TEST_API_KEY,
        model=Config.AI_TEST_MODEL
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "message" in data


@allure.feature("Real Project GenAI QA")
@allure.story("Embedding Provider Connectivity")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_embedding_provider_connectivity():
    if not Config.AI_EMBEDDING_API_KEY:
        pytest.skip("AI_EMBEDDING_API_KEY is not configured")

    api = CloudPOSAPIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.test_embedding_provider(
        openai_api_key=Config.AI_EMBEDDING_API_KEY,
        embedding_model=Config.AI_EMBEDDING_MODEL
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

