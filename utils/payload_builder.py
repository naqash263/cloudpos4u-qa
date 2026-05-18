from datetime import datetime, timezone


class PayloadBuilder:

    @staticmethod
    def cash_paid_order(dish, customer_name="Automation Test Customer"):
        return {
            "customerDetails": {
                "name": customer_name,
                "phone": "971500000000",
                "email": "automation@example.com",
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
            "notes": "Created by automation test"
        }