import os
import allure
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("UI Authentication")
@allure.story("Valid Admin Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_login_success(driver):
    base_url = os.getenv("BASE_URL")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")

    login_page = LoginPage(driver)

    with allure.step("Open admin login page"):
        login_page.load(base_url)

    with allure.step("Login with valid admin credentials"):
        login_page.login(email, password)

    with allure.step("Verify user is redirected away from login page"):
        assert "login" not in driver.current_url.lower()