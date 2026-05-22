import pytest
import allure

from ai_qa.parsers.json_output_parser import JSONOutputParser


@pytest.mark.ai
@pytest.mark.regression
@allure.feature("AI Contract Testing")
@allure.story("Valid AI Order Extraction JSON Contract")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_ai_order_extraction_contract():
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
          "name": "Sweet Lassi",
          "quantity": 1
        }
      ],
      "unavailableItems": [],
      "needsConfirmation": true
    }
    """

    with allure.step("Parse LLM JSON output"):
        parsed_data = JSONOutputParser.parse(raw_output)

    with allure.step("Validate AI order extraction contract"):
        assert JSONOutputParser.validate_order_extraction_schema(parsed_data) is True


@pytest.mark.ai
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("AI Contract Testing")
@allure.story("AI Output Missing Required Field")
@allure.severity(allure.severity_level.NORMAL)
def test_ai_order_extraction_missing_required_field_should_fail():
    raw_output = """
    {
      "intent": "create_order",
      "items": [
        {
          "name": "Chicken Biryani",
          "quantity": 2
        }
      ]
    }
    """

    parsed_data = JSONOutputParser.parse(raw_output)

    with pytest.raises(ValueError, match="Missing required field: orderType"):
        JSONOutputParser.validate_order_extraction_schema(parsed_data)


@pytest.mark.ai
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("AI Contract Testing")
@allure.story("AI Output Invalid JSON")
@allure.severity(allure.severity_level.NORMAL)
def test_ai_order_extraction_invalid_json_should_fail():
    raw_output = """
    {
      "intent": "create_order",
      "orderType": "Takeaway",
      "items": [
        {
          "name": "Chicken Biryani",
          "quantity": 2
        }
      ]
    """

    with pytest.raises(ValueError, match="Invalid JSON output"):
        JSONOutputParser.parse(raw_output)


@pytest.mark.ai
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("AI Contract Testing")
@allure.story("AI Output Empty Items")
@allure.severity(allure.severity_level.NORMAL)
def test_ai_order_extraction_empty_items_should_fail():
    raw_output = """
    {
      "intent": "create_order",
      "orderType": "Takeaway",
      "paymentMethod": "Unknown",
      "items": [],
      "unavailableItems": [],
      "needsConfirmation": true
    }
    """

    parsed_data = JSONOutputParser.parse(raw_output)

    with pytest.raises(ValueError, match="Field 'items' must not be empty"):
        JSONOutputParser.validate_order_extraction_schema(parsed_data)


@pytest.mark.ai
@pytest.mark.negative
@pytest.mark.regression
@allure.feature("AI Contract Testing")
@allure.story("AI Output Invalid Quantity Type")
@allure.severity(allure.severity_level.NORMAL)
def test_ai_order_extraction_invalid_quantity_type_should_fail():
    raw_output = """
    {
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
      "needsConfirmation": true
    }
    """

    parsed_data = JSONOutputParser.parse(raw_output)

    with pytest.raises(ValueError, match="Item quantity must be integer at index 0"):
        JSONOutputParser.validate_order_extraction_schema(parsed_data)