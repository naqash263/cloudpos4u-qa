class OrderExtractionPromptBuilder:

    @staticmethod
    def build(user_message):
        return f"""
Extract restaurant order details from the customer message.

Customer message:
{user_message}

Return only valid JSON using this exact schema:

{{
  "intent": "create_order",
  "orderType": "Takeaway",
  "paymentMethod": "Unknown",
  "items": [
    {{
      "name": "Item name",
      "quantity": 1
    }}
  ],
  "unavailableItems": [],
  "needsConfirmation": true
}}

Rules:
- intent must be one of: create_order, menu_query, cancel_order, unknown
- orderType must be one of: Takeaway, Dine-in, Delivery, Unknown
- paymentMethod must be one of: Cash, Card, Online, Unknown
- quantity must be integer
- needsConfirmation must be true unless user clearly confirms final order
- Return JSON only
"""