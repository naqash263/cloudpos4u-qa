import json


class JSONOutputParser:
    """
    Extracts and validates JSON object from LLM output.

    This is useful because local LLMs sometimes return:
    - reasoning text before JSON
    - markdown code fences
    - explanation after JSON
    """

    @staticmethod
    def extract_json(raw_output: str) -> dict:
        if not raw_output or not raw_output.strip():
            raise ValueError("LLM output is empty")

        cleaned = raw_output.strip()

        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

        start_index = cleaned.find("{")
        end_index = cleaned.rfind("}")

        if start_index == -1 or end_index == -1:
            raise ValueError("No JSON object found in LLM output")

        json_text = cleaned[start_index:end_index + 1]

        try:
            return json.loads(json_text)
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON extracted from LLM output: {error}")

    @staticmethod
    def validate_order_extraction_schema(parsed_json: dict) -> bool:
        required_fields = [
            "intent",
            "orderType",
            "paymentMethod",
            "items",
            "unavailableItems",
            "needsConfirmation"
        ]

        for field in required_fields:
            if field not in parsed_json:
                raise ValueError(f"Missing required field: {field}")

        if not isinstance(parsed_json["items"], list):
            raise ValueError("items must be a list")

        if not isinstance(parsed_json["unavailableItems"], list):
            raise ValueError("unavailableItems must be a list")

        if not isinstance(parsed_json["needsConfirmation"], bool):
            raise ValueError("needsConfirmation must be boolean")

        for item in parsed_json["items"]:
            if "name" not in item:
                raise ValueError("Each item must contain name")

            if "quantity" not in item:
                raise ValueError("Each item must contain quantity")

            if not isinstance(item["quantity"], int):
                raise ValueError("Item quantity must be integer")

        return True