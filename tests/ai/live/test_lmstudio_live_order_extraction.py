import os
import pytest
import allure

from ai_qa.lmstudio_client import LMStudioClient
from ai_qa.order_extraction_prompt_builder import OrderExtractionPromptBuilder
from ai_qa.parsers.json_output_parser import JSONOutputParser


pytestmark = pytest.mark.skipif(
    os.getenv("RUN_LMSTUDIO_TESTS", "false").lower() != "true",
    reason="LM Studio live tests require RUN_LMSTUDIO_TESTS=true and local server running"
)


@pytest.mark.ai
@pytest.mark.regression
@allure.feature("AI Live Testing")
@allure.story("LM Studio Order Extraction")
@allure.severity(allure.severity_level.CRITICAL)
def test_lmstudio_extracts_takeaway_order_from_customer_message():
    user_message = "I want 2 chicken biryani and 1 sweet lassi for takeaway"

    with allure.step("Build order extraction prompt"):
        prompt = OrderExtractionPromptBuilder.build(user_message)

    with allure.step("Send prompt to LM Studio local model"):
        client = LMStudioClient()
        raw_output = client.chat(prompt)

    with allure.step("Parse LLM JSON output"):
        parsed = JSONOutputParser.extract_json(raw_output)

    with allure.step("Validate LLM output contract"):
        assert JSONOutputParser.validate_order_extraction_schema(parsed) is True

    with allure.step("Validate extracted order fields"):
        assert parsed["intent"] == "create_order"
        assert parsed["orderType"] == "Takeaway"
        assert len(parsed["items"]) == 2

        item_names = [item["name"].lower() for item in parsed["items"]]

        assert any("biryani" in name for name in item_names)
        assert any("lassi" in name for name in item_names)

        quantities = {
            item["name"].lower(): item["quantity"]
            for item in parsed["items"]
        }

        assert any(quantity == 2 for name, quantity in quantities.items() if "biryani" in name)
        assert any(quantity == 1 for name, quantity in quantities.items() if "lassi" in name)