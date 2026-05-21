import allure
import pytest

from utils.payload_builder import PayloadBuilder

@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("API Order Management")
@allure.story("Create Cash Paid Order API")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_cash_paid_order_api(authenticated_api_client, available_dish):
    payload = PayloadBuilder.cash_paid_order(
        available_dish,
        customer_name="API Test Customer"
    )

    response = authenticated_api_client.create_order(payload)

    assert response.status_code == 201

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "Order created!"
    assert data["data"]["orderNumber"] is not None
    assert data["data"]["customerName"] == "API Test Customer"
    assert data["data"]["paymentMethod"] == "Cash"
    assert data["data"]["paymentStatus"] == "Paid"
    assert data["data"]["orderType"] == "Takeaway"
    assert data["data"]["branchId"] == authenticated_api_client.branch_id
    assert len(data["data"]["items"]) > 0

@pytest.mark.api
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("API Order Management")
@allure.story("Create Order Without Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_order_without_auth_should_fail(authenticated_api_client, available_dish):
    payload = PayloadBuilder.cash_paid_order(
        available_dish,
        customer_name="Unauthorized Test Customer"
    )

    authenticated_api_client.token = None

    response = authenticated_api_client.create_order(payload)

    assert response.status_code == 401

    data = response.json()

    assert data["status"] == 401
    assert "Authentication required" in data["message"]