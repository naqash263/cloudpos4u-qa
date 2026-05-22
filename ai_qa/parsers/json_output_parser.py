import json
import re


class JSONOutputParser:
    @staticmethod
    def parse(raw_output):
        return JSONOutputParser.extract_json(raw_output)

    @staticmethod
    def extract_json(raw_output):
        if not raw_output or not raw_output.strip():
            raise ValueError("LLM output is empty")

        cleaned_output = raw_output.strip()

        # Case 1: clean JSON
        try:
            return json.loads(cleaned_output)
        except json.JSONDecodeError:
            pass

        # Case 2: markdown json code block
        code_block_match = re.search(
            r"```(?:json)?\s*(\{.*?\})\s*```",
            cleaned_output,
            re.DOTALL
        )

        if code_block_match:
            json_text = code_block_match.group(1)

            try:
                return json.loads(json_text)
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid JSON output: {error}") from error

        # Case 3: reasoning text before/after JSON
        json_match = re.search(r"\{.*\}", cleaned_output, re.DOTALL)

        if not json_match:
            raise ValueError("No JSON object found in LLM output")

        json_text = json_match.group(0)

        try:
            return json.loads(json_text)
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSON output: {error}") from error

    @staticmethod
    def validate_order_extraction_schema(data):
        required_fields = [
            "intent",
            "orderType",
            "paymentMethod",
            "items",
            "unavailableItems",
            "needsConfirmation"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        if not isinstance(data["intent"], str):
            raise ValueError("Field 'intent' must be a string")

        if not isinstance(data["orderType"], str):
            raise ValueError("Field 'orderType' must be a string")

        if not isinstance(data["paymentMethod"], str):
            raise ValueError("Field 'paymentMethod' must be a string")

        if not isinstance(data["items"], list):
            raise ValueError("Field 'items' must be a list")

        if len(data["items"]) == 0:
            raise ValueError("Field 'items' must not be empty")

        if not isinstance(data["unavailableItems"], list):
            raise ValueError("Field 'unavailableItems' must be a list")

        if not isinstance(data["needsConfirmation"], bool):
            raise ValueError("Field 'needsConfirmation' must be a boolean")

        for index, item in enumerate(data["items"]):
            if "name" not in item:
                raise ValueError(f"Missing item name at index {index}")

            if "quantity" not in item:
                raise ValueError(f"Missing item quantity at index {index}")

            if not isinstance(item["name"], str):
                raise ValueError(f"Item name must be string at index {index}")

            if not isinstance(item["quantity"], int):
                raise ValueError(f"Item quantity must be integer at index {index}")

            if item["quantity"] <= 0:
                raise ValueError(f"Item quantity must be greater than zero at index {index}")

        return True