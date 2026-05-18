from utils.config import Config
from utils.api_client import APIClient
from utils.payload_builder import PayloadBuilder


def test_create_cash_paid_order_api():
    api = APIClient(Config.API_BASE_URL)

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
        customer_name="API Test Customer"
    )

    response = api.create_order(payload)

    assert response.status_code == 201

    data = response.json()

    assert data["success"] is True
    assert data["message"] == "Order created!"
    assert data["data"]["orderNumber"] is not None
    assert data["data"]["customerName"] == "API Test Customer"
    assert data["data"]["paymentMethod"] == "Cash"
    assert data["data"]["paymentStatus"] == "Paid"
    assert data["data"]["orderType"] == "Takeaway"
    assert data["data"]["branchId"] == api.branch_id
    assert len(data["data"]["items"]) > 0


def test_create_order_without_auth_should_fail():
    api = APIClient(Config.API_BASE_URL)

    # Login only to get a valid dish, then remove auth token intentionally
    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    dishes_response = api.get_all_dishes()
    dishes = dishes_response.json()["data"]

    available_dishes = [
        dish for dish in dishes
        if dish["isAvailable"] is True and dish["branchId"] == api.branch_id
    ]

    assert len(available_dishes) > 0

    payload = PayloadBuilder.cash_paid_order(
        available_dishes[0],
        customer_name="Unauthorized Test Customer"
    )

    api.token = None

    response = api.create_order(payload)

    assert response.status_code == 401

    data = response.json()

    assert data["status"] == 401
    assert "Authentication required" in data["message"]