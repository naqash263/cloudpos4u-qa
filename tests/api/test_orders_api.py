import allure
from utils.config import Config
from utils.api_client import APIClient
from utils.payload_builder import PayloadBuilder


@allure.feature("API Order Management")
@allure.story("Create Cash Paid Order API")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_cash_paid_order_api():
    api = APIClient(Config.API_BASE_URL)

    with allure.step("Login and get access token"):
        login_response = api.login(
            Config.ADMIN_EMAIL,
            Config.ADMIN_PASSWORD
        )

        assert login_response.status_code == 200

    with allure.step("Fetch available dishes"):
        dishes_response = api.get_all_dishes()
        assert dishes_response.status_code == 200

        dishes = dishes_response.json()["data"]

        available_dishes = [
            dish for dish in dishes
            if dish["isAvailable"] is True and dish["branchId"] == api.branch_id
        ]

        assert len(available_dishes) > 0

    with allure.step("Build cash paid order payload"):
        payload = PayloadBuilder.cash_paid_order(
            available_dishes[0],
            customer_name="API Test Customer"
        )

    with allure.step("Create order through API"):
        response = api.create_order(payload)

    with allure.step("Validate order creation response"):
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


@allure.feature("API Order Management")
@allure.story("Create Order Without Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_order_without_auth_should_fail():
    api = APIClient(Config.API_BASE_URL)

    with allure.step("Login only to fetch valid dish data"):
        login_response = api.login(
            Config.ADMIN_EMAIL,
            Config.ADMIN_PASSWORD
        )

        assert login_response.status_code == 200

    with allure.step("Fetch available dishes"):
        dishes_response = api.get_all_dishes()
        dishes = dishes_response.json()["data"]

        available_dishes = [
            dish for dish in dishes
            if dish["isAvailable"] is True and dish["branchId"] == api.branch_id
        ]

        assert len(available_dishes) > 0

    with allure.step("Build order payload"):
        payload = PayloadBuilder.cash_paid_order(
            available_dishes[0],
            customer_name="Unauthorized Test Customer"
        )

    with allure.step("Remove authentication token intentionally"):
        api.token = None

    with allure.step("Attempt to create order without authentication"):
        response = api.create_order(payload)

    with allure.step("Validate unauthorized response"):
        assert response.status_code == 401

        data = response.json()

        assert data["status"] == 401
        assert "Authentication required" in data["message"]