import json
from pathlib import Path

import pytest
import allure

from utils.config import Config
from pages.login_page import LoginPage


ROUTES_FILE = Path("tests/data/discovered_ui_smoke_routes.json")


def load_discovered_ui_routes():
    with open(ROUTES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login_page = LoginPage(driver)

    login_page.load(Config.BASE_URL)
    login_page.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    return driver


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Discovery UI Smoke Tests")
@allure.story("Discovered Frontend Routes Load Successfully")
@pytest.mark.parametrize("route_config", load_discovered_ui_routes())
def test_discovered_ui_route_loads_successfully(logged_in_driver, route_config):
    route = route_config["route"]
    expected_url_contains = route_config["expected_url_contains"]

    target_url = f"{Config.BASE_URL.rstrip('/')}{route}"

    with allure.step(f"Open discovered UI route: {route}"):
        logged_in_driver.get(target_url)

    with allure.step("Validate route did not redirect to auth page"):
        assert "/auth" not in logged_in_driver.current_url

    with allure.step("Validate expected URL fragment"):
        assert expected_url_contains in logged_in_driver.current_url
