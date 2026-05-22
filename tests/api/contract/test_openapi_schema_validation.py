import yaml
import pytest
import allure
from pathlib import Path
from openapi_spec_validator import validate


OPENAPI_FILE = Path("contracts/openapi/cloudpos4u.openapi.yaml")


@pytest.mark.api
@pytest.mark.regression
@allure.feature("API Contract Testing")
@allure.story("Validate OpenAPI Specification")
@allure.severity(allure.severity_level.CRITICAL)
def test_openapi_spec_is_valid():
    assert OPENAPI_FILE.exists(), f"OpenAPI file not found: {OPENAPI_FILE}"

    with allure.step("Load OpenAPI YAML file"):
        with open(OPENAPI_FILE, "r", encoding="utf-8") as file:
            spec = yaml.safe_load(file)

    with allure.step("Validate OpenAPI schema format"):
        validate(spec)


@pytest.mark.api
@pytest.mark.regression
@allure.feature("API Contract Testing")
@allure.story("Validate Required CloudPOS4U Endpoints Exist In OpenAPI")
@allure.severity(allure.severity_level.CRITICAL)
def test_required_endpoints_exist_in_openapi_contract():
    with open(OPENAPI_FILE, "r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    paths = spec.get("paths", {})

    assert "/user/login" in paths
    assert "/dish/all" in paths
    assert "/order/" in paths

    assert "post" in paths["/user/login"]
    assert "get" in paths["/dish/all"]
    assert "post" in paths["/order/"]


@pytest.mark.api
@pytest.mark.regression
@allure.feature("API Contract Testing")
@allure.story("Validate Order API Contract Has Required Payload Fields")
@allure.severity(allure.severity_level.NORMAL)
def test_create_order_contract_has_required_payload_fields():
    with open(OPENAPI_FILE, "r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    order_schema = (
        spec["paths"]["/order/"]["post"]["requestBody"]["content"]
        ["application/json"]["schema"]
    )

    required_fields = order_schema.get("required", [])

    assert "customerDetails" in required_fields
    assert "orderType" in required_fields
    assert "bills" in required_fields
    assert "items" in required_fields
    assert "paymentMethod" in required_fields
    assert "paymentStatus" in required_fields