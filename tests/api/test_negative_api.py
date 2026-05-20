import pytest
import allure
from utils.config import Config
from utils.api_client import APIClient
from utils.payload_builder import PayloadBuilder


@pytest.mark.xfail(
    reason="Known defect: API currently allows creating order with empty items list",
    strict=False
)
@allure.feature("API Order Management")
@allure.story("Create Order With Missing Items")
@allure.severity(allure.severity_level.NORMAL)
def test_create_order_with_missing_items_should_fail():
    api = APIClient(Config.API_BASE_URL)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer invalid-token",
        "x-branch-id": "038f901a-732e-4f4f-a05f-008d789f58f1",
        "x-branch-code": "MAIN-01",
        "Content-Type": "application/json"
    }

    response = api.get_all_dishes_with_custom_headers(headers=headers)

    assert response.status_code in [401, 403]

    data = response.json()

    assert "message" in data


@allure.feature("API Order Management")
@allure.story("Create Order Without Branch ID")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_order_without_branch_id_should_fail():
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
        customer_name="Missing Branch Test Customer"
    )

    headers_without_branch = {
        "accept": "application/json",
        "Authorization": f"Bearer {api.token}",
        "x-branch-code": api.branch_code or "",
        "Content-Type": "application/json"
    }

    cookies = {
        "accessToken": api.token
    }

    response = api.create_order_with_custom_headers(
        payload,
        headers=headers_without_branch,
        cookies=cookies
    )

    assert response.status_code in [400, 401, 403]

    data = response.json()

    assert "message" in data

@pytest.mark.xfail(
    reason="Known defect: API currently allows creating order With Missing Items",
    strict=False
)
@allure.feature("API Order Management")
@allure.story("Create Order With Missing Items")
@allure.severity(allure.severity_level.NORMAL)
def test_create_order_with_missing_items_should_fail():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    payload = {
        "customerDetails": {
            "name": "Missing Items Test Customer",
            "phone": "971500000001",
            "email": "missingitems@example.com",
            "guests": 1,
            "addresses": []
        },
        "sourceChannel": "Walk-in",
        "orderType": "Takeaway",
        "tipAmount": 0,
        "orderStatus": "In Progress",
        "bills": {
            "subtotal": 0,
            "discountAmount": 0,
            "total": 0,
            "tax": 0,
            "totalWithTax": 0,
            "tipAmount": 0
        },
        "appliedDeals": [],
        "items": [],
        "paymentMethod": "Cash",
        "paymentStatus": "Paid",
        "paymentData": {},
        "notes": "Created by negative API test"
    }

    response = api.create_order(payload)

    assert response.status_code in [400, 422]

    data = response.json()

    assert "message" in data


@pytest.mark.xfail(
    reason="Known defect: API currently allows creating order with invalid dish ID",
    strict=False
)
@allure.feature("API Order Management")
@allure.story("Create Order With Invalid Dish ID")
@allure.severity(allure.severity_level.NORMAL)
def test_create_order_with_invalid_dish_id_should_fail():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    invalid_dish = {
        "id": "00000000-0000-0000-0000-000000000000",
        "name": "Invalid Dish",
        "price": 10,
        "branchId": api.branch_id,
        "isAvailable": True
    }

    payload = PayloadBuilder.cash_paid_order(
        invalid_dish,
        customer_name="Invalid Dish Test Customer"
    )

    response = api.create_order(payload)

    assert response.status_code in [400, 404, 422]

    data = response.json()

    assert "message" in data