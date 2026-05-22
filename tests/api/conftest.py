import pytest

from utils.config import Config
from utils.api.cloudpos_api_client import CloudPOSAPIClient


@pytest.fixture
def api_client():
    return CloudPOSAPIClient(Config.API_BASE_URL)


@pytest.fixture
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


@pytest.fixture
def available_dish(authenticated_api_client):
    response = authenticated_api_client.get_all_dishes()

    assert response.status_code == 200

    dishes = response.json()["data"]

    available_dishes = [
        dish for dish in dishes
        if dish["isAvailable"] is True
        and dish["branchId"] == authenticated_api_client.branch_id
    ]

    assert len(available_dishes) > 0

    return available_dishes[0]