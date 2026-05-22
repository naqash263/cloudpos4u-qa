import pytest
import allure
from jsonschema import validate

from utils.config import Config
from utils.api.cloudpos_api_client import CloudPOSAPIClient
from utils.payload_builder import PayloadBuilder
from tests.helpers.openapi_schema_helper import OpenAPISchemaHelper


@pytest.mark.api
@pytest.mark.regression
@allure.feature("API Contract Testing")
@allure.story("Live Login API Response Matches OpenAPI Contract")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_response_matches_openapi_contract():
    api = CloudPOSAPIClient(Config.API_BASE_URL)

    response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert response.status_code == 200

    schema = OpenAPISchemaHelper.get_component_schema("LoginSuccessResponse")

    validate(instance=response.json(), schema=schema)


@pytest.mark.api
@pytest.mark.regression
@allure.feature("API Contract Testing")
@allure.story("Live Dish API Response Matches OpenAPI Contract")
@allure.severity(allure.severity_level.CRITICAL)
def test_dish_list_response_matches_openapi_contract():
    api = CloudPOSAPIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    response = api.get_all_dishes()

    assert response.status_code == 200

    schema = OpenAPISchemaHelper.get_component_schema("DishListResponse")

    validate(instance=response.json(), schema=schema)


@pytest.mark.api
@pytest.mark.regression
@allure.feature("API Contract Testing")
@allure.story("Live Create Order API Response Matches OpenAPI Contract")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_order_response_matches_openapi_contract():
    api = CloudPOSAPIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    dishes_response = api.get_all_dishes()
    assert dishes_response.status_code == 200

    dishes = dishes_response.json()["data"]

    available_dishes = [
        dish for dish in dishes
        if dish["isAvailable"] is True and dish["branchId"] == api.branch_id
    ]

    assert len(available_dishes) > 0

    payload = PayloadBuilder.cash_paid_order(
        available_dishes[0],
        customer_name="Contract Test Customer"
    )

    response = api.create_order(payload)

    assert response.status_code == 201

    schema = OpenAPISchemaHelper.get_component_schema("OrderCreatedResponse")

    validate(instance=response.json(), schema=schema)