import pytest

from utils.config import Config
from utils.api.cloudpos_api_client import CloudPOSAPIClient


@pytest.fixture
def ai_api_client():
    return CloudPOSAPIClient(Config.API_BASE_URL)


@pytest.fixture
def authenticated_ai_api_client():
    api = CloudPOSAPIClient(Config.API_BASE_URL)

    response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert response.status_code == 200
    assert api.token is not None
    assert api.branch_id is not None

    return api