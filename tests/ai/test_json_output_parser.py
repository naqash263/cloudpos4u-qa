import pytest
import allure
from ai_qa.parsers.json_output_parser import JSONOutputParser

@allure.feature("GenAI QA")
@allure.story("LLM JSON Output Parser")
@allure.severity(allure.severity_level.CRITICAL)
def test_parser_accepts_clean_json():
    raw_output = """
    {
      "intent": "create_order",
      "orderType": "Takeaway",
      "paymentMethod": "Unknown",
      "items": [
        {
          "name": "Chicken Biryani",
          "quantity": 2
        },
        {
          "name": "Lassi (Sweet)",
          "quantity": 1
        }
      ],
      "unavailableItems": [],
      "needsConfirmation": true
    }
    """

    parsed = JSONOutputParser.extract_json(raw_output)

    assert parsed["intent"] == "create_order"
    assert parsed["orderType"] == "Takeaway"
    assert parsed["items"][0]["name"] == "Chicken Biryani"

    assert JSONOutputParser.validate_order_extraction_schema(parsed) is True


def test_parser_extracts_json_from_reasoning_text():
    raw_output = """
    Okay, let's break this down.

    The user wants 2 chicken biryani and 1 sweet lassi for takeaway.

    {
      "intent": "create_order",
      "orderType": "Takeaway",
      "paymentMethod": "Unknown",
      "items": [
        {
          "name": "Chicken Biryani",
          "quantity": 2
        },
        {
          "name": "Lassi (Sweet)",
          "quantity": 1
        }
      ],
      "unavailableItems": [],
      "needsConfirmation": true
    }
    """

    parsed = JSONOutputParser.extract_json(raw_output)

    assert parsed["intent"] == "create_order"
    assert parsed["orderType"] == "Takeaway"
    assert len(parsed["items"]) == 2

    assert JSONOutputParser.validate_order_extraction_schema(parsed) is True


def test_parser_extracts_json_from_markdown_code_block():
    raw_output = """
    ```json
    {
      "intent": "menu_query",
      "orderType": "Unknown",
      "paymentMethod": "Unknown",
      "items": [
        {
          "name": "Kulfi Falooda",
          "quantity": 1
        }
      ],
      "unavailableItems": [],
      "needsConfirmation": true
    }
    ```
    """

    parsed = JSONOutputParser.extract_json(raw_output)

    assert parsed["intent"] == "menu_query"
    assert parsed["items"][0]["name"] == "Kulfi Falooda"

    assert JSONOutputParser.validate_order_extraction_schema(parsed) is True


def test_parser_fails_when_no_json_found():
    raw_output = "I cannot process this request."

    with pytest.raises(ValueError, match="No JSON object found"):
        JSONOutputParser.extract_json(raw_output)

@allure.feature("GenAI QA")
@allure.story("LLM Output Schema Validation")
@allure.severity(allure.severity_level.NORMAL)
def test_schema_validation_fails_when_required_field_missing():
    parsed_json = {
        "intent": "create_order",
        "orderType": "Takeaway",
        "items": []
    }

    with pytest.raises(ValueError, match="Missing required field"):
        JSONOutputParser.validate_order_extraction_schema(parsed_json)


def test_schema_validation_fails_when_quantity_is_not_integer():
    parsed_json = {
        "intent": "create_order",
        "orderType": "Takeaway",
        "paymentMethod": "Unknown",
        "items": [
            {
                "name": "Chicken Biryani",
                "quantity": "two"
            }
        ],
        "unavailableItems": [],
        "needsConfirmation": True
    }

    with pytest.raises(ValueError, match="Item quantity must be integer"):
        JSONOutputParser.validate_order_extraction_schema(parsed_json)