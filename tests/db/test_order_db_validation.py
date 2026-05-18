from datetime import datetime, timezone
from utils.api_client import APIClient
from utils.db_client import DBClient
from utils.config import Config


def test_order_saved_in_database():
    api = APIClient(Config.API_BASE_URL)

    login_response = api.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    assert login_response.status_code == 200

    dishes_response = api.get_all_dishes()
    dishes = dishes_response.json()["data"]

    dish = dishes[0]

    payload = {
        "customerDetails": {
            "name": "DB Test Customer",
            "phone": "971500000000",
            "email": "dbtest@example.com",
            "guests": 1,
            "addresses": []
        },
        "sourceChannel": "Walk-in",
        "orderType": "Takeaway",
        "tipAmount": 0,
        "orderStatus": "In Progress",
        "orderDate": datetime.now(timezone.utc).isoformat(),
        "bills": {
            "subtotal": dish["price"],
            "discountAmount": 0,
            "total": dish["price"],
            "tax": 0,
            "totalWithTax": dish["price"],
            "tipAmount": 0
        },
        "appliedDeals": [],
        "items": [
            {
                "id": dish["id"],
                "dishId": dish["id"],
                "name": dish["name"],
                "price": dish["price"],
                "pricePerQuantity": dish["price"],
                "quantity": 1
            }
        ],
        "paymentMethod": "Cash",
        "paymentStatus": "Paid",
        "paymentData": {},
        "notes": "DB validation test"
    }

    response = api.create_order(payload)

    assert response.status_code == 201

    order_data = response.json()["data"]
    order_number = order_data["orderNumber"]

    db = DBClient()

    db_order = db.get_order_by_order_number(order_number)

    assert db_order is not None
    assert db_order[1] == order_number
    assert db_order[2] == "DB Test Customer"
    assert db_order[3] == "Cash"
    assert db_order[4] == "Paid"
    assert db_order[5] == "Takeaway"

    db.close()