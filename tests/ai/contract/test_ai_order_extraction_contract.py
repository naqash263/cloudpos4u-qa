import json
from pathlib import Path

import allure
import pytest

from ai_qa.parsers.json_output_parser import JSONOutputParser


DATA_FILE = Path("ai_qa/samples/llm_outputs/order_extraction_outputs.json")


def load_test_cases():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def item_exists(items, expected_name, expected_quantity):
    return any(
        item["name"] == expected_name and item["quantity"] == expected_quantity
        for item in items
    )


@allure.feature("GenAI QA")
@allure.story("AI Order Extraction Contract")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("case", load_test_cases(), ids=lambda case: case["case_id"])
def test_ai_order_extraction_contract(case):
    raw_output = json.dumps(case["raw_output"])

    with allure.step("Parse LLM output JSON"):
        parsed = JSONOutputParser.extract_json(raw_output)

    with allure.step("Validate required AI output schema"):
        assert JSONOutputParser.validate_order_extraction_schema(parsed) is True

    with allure.step("Validate intent"):
        assert parsed["intent"] == case["expected"]["intent"]

    with allure.step("Validate order type"):
        assert parsed["orderType"] == case["expected"]["orderType"]

    with allure.step("Validate expected items and quantities"):
        for expected_item in case["expected"].get("items", []):
            assert item_exists(
                parsed["items"],
                expected_item["name"],
                expected_item["quantity"]
            )

    with allure.step("Validate unavailable items when expected"):
        expected_unavailable = case["expected"].get("unavailableItems", [])

        for unavailable_item in expected_unavailable:
            assert unavailable_item in parsed["unavailableItems"]