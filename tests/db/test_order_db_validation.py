import pytest
import allure

from utils.config import Config
from utils.api.cloudpos_api_client import CloudPOSAPIClient
from utils.payload_builder import PayloadBuilder
from utils.db_client import DBClient


pytestmark = pytest.mark.skipif(
    not Config.RUN_DB_TESTS,
    reason="DB tests require active SSH tunnel and RUN_DB_TESTS=true"
)


@pytest.mark.db
@pytest.mark.api
@pytest.mark.regression
@allure.feature("Database Validation")
@allure.story("API Created Order Exists In Tenant Schema Database")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_created_api_should_exist_in_database():
    api = CloudPOSAPIClient(Config.API_BASE_URL)

    customer_name = "DB Validation Customer"
    order_number = None

    with allure.step("Login and get authenticated branch context"):
        login_response = api.login(
            Config.ADMIN_EMAIL,
            Config.ADMIN_PASSWORD
        )

        assert login_response.status_code == 200
        assert api.token is not None
        assert api.branch_id is not None

    with allure.step("Fetch available dish for order payload"):
        dishes_response = api.get_all_dishes()

        assert dishes_response.status_code == 200

        dishes = dishes_response.json()["data"]

        available_dishes = [
            dish for dish in dishes
            if dish["isAvailable"] is True and dish["branchId"] == api.branch_id
        ]

        assert len(available_dishes) > 0

    with allure.step("Create cash paid order through API"):
        payload = PayloadBuilder.cash_paid_order(
            available_dishes[0],
            customer_name=customer_name
        )

        response = api.create_order(payload)

        assert response.status_code == 201

        response_json = response.json()
        order_data = response_json["data"]

        order_number = order_data["orderNumber"]

        assert order_number is not None
        assert order_data["customerName"] == customer_name
        assert order_data["paymentMethod"] == "Cash"
        assert order_data["paymentStatus"] == "Paid"
        assert order_data["orderType"] == "Takeaway"
        assert order_data["branchId"] == api.branch_id

    with allure.step("Validate created order exists in PostgreSQL tenant schema"):
        assert order_number is not None, "Order number was not returned from API response"

        db = DBClient()

        try:
            db_order = db.get_order_by_order_number(order_number)

            assert db_order is not None, f"Order not found in DB: {order_number}"

            db_order_number = db_order[1]
            db_customer_name = db_order[2]
            db_order_type = db_order[5]
            db_payment_method = db_order[6]
            db_payment_status = db_order[7]
            db_branch_id = db_order[8]

            assert db_order_number == order_number
            assert db_customer_name == customer_name
            assert db_order_type == "Takeaway"
            assert db_payment_method == "Cash"
            assert db_payment_status == "Paid"
            assert db_branch_id == api.branch_id

        finally:
            db.close()