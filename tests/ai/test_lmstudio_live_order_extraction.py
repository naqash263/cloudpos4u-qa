import allure
import pytest

from ai_qa.lmstudio_client import LMStudioClient
from ai_qa.order_extraction_prompt_builder import build_order_extraction_prompt
from ai_qa.parsers.json_output_parser import JSONOutputParser


def item_exists(items, expected_name, expected_quantity):
    return any(
        item["name"] == expected_name and item["quantity"] == expected_quantity
        for item in items
    )


@allure.feature("GenAI QA")
@allure.story("Live LM Studio Order Extraction")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ai_live
def test_lmstudio_extracts_takeaway_order_live():
    customer_message = "I want 2 chicken biryani and 1 sweet lassi for takeaway"

    with allure.step("Build CloudPOS4U order extraction prompt"):
        prompt = build_order_extraction_prompt(customer_message)

    with allure.step("Call LM Studio local model"):
        client = LMStudioClient()
        raw_output = client.chat(prompt)

    with allure.step("Parse model output JSON"):
        parsed = JSONOutputParser.extract_json(raw_output)

    with allure.step("Validate required AI output schema"):
        assert JSONOutputParser.validate_order_extraction_schema(parsed) is True

    with allure.step("Validate business extraction fields"):
        assert parsed["intent"] == "create_order"
        assert parsed["orderType"] == "Takeaway"
        assert item_exists(parsed["items"], "Chicken Biryani", 2)
        assert item_exists(parsed["items"], "Lassi (Sweet)", 1)
        assert parsed["needsConfirmation"] is True