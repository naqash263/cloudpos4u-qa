import allure
import pytest


@allure.feature("Real Project GenAI QA")
@allure.story("AI Staff Assistant Analytics Query")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ai_api
def test_ai_staff_assistant_analytics_query(authenticated_ai_api_client):
    response = authenticated_ai_api_client.ask_staff_ai(
        "Give me a short sales performance summary for this branch."
    )

    if response.status_code == 403:
        pytest.skip(
            f"AI staff assistant endpoint is not enabled or not permitted in this environment: {response.text}"
        )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"].strip()) > 0

    ai_response = data["response"].lower()

    analytics_keywords = [
        "sales",
        "revenue",
        "order",
        "orders",
        "performance",
        "summary",
        "profit",
        "margin",
        "analytics",
        "branch",
        "days",
        "report"
    ]

    assert any(keyword in ai_response for keyword in analytics_keywords)


@allure.feature("Real Project GenAI QA")
@allure.story("AI Staff Assistant Analytics Scope Control")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ai_api
def test_ai_staff_assistant_menu_scope_limitation(authenticated_ai_api_client):
    response = authenticated_ai_api_client.ask_staff_ai(
        "List 3 available menu items from this branch menu."
    )
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "response" in data

    ai_response = data["response"].lower()

    safe_scope_keywords = [
        "sales data",
        "menu",
        "product catalog",
        "catalog",
        "access",
        "cannot",
        "can't",
        "unable",
        "need"
    ]

    assert any(keyword in ai_response for keyword in safe_scope_keywords)
