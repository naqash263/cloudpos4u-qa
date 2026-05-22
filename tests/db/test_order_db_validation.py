import pytest
import allure
from utils.config import Config
from utils.api.cloudpos_api_client import cloudpos_api_client
from utils.payload_builder import PayloadBuilder
from utils.db_client import DBClient


@pytest.mark.db
@pytest.mark.api
@pytest.mark.regression
@allure.feature("Database Validation")
@allure.story("Order Created Through API Exists In Database")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_created_api_should_exist_in_database():
    api = cloudpos_api_client(Config.API_BASE_URL)

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

    with allure.step("Create order through API"):
        payload = PayloadBuilder.cash_paid_order(
            available_dishes[0],
            customer_name="DB Validation Customer"
        )

        response = api.create_order(payload)

        assert response.status_code == 201

        order_data = response.json()["data"]
        order_number = order_data["orderNumber"]

    with allure.step("Verify order exists in PostgreSQL database"):
        db = DBClient()

        try:
            db_order = db.get_order_by_order_number(order_number)

            assert db_order is not None

            assert db_order[1] == order_number
            assert db_order[2] == "DB Validation Customer"
            assert db_order[5] == "Takeaway"
            assert db_order[6] == "Cash"
            assert db_order[7] == "Paid"
            assert db_order[8] == api.branch_id

        finally:
            db.close()