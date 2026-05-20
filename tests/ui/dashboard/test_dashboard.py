import os
import allure
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

load_dotenv()


@allure.feature("UI Dashboard")
@allure.story("Dashboard Load After Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_dashboard_load_after_login(driver):
    base_url = os.getenv("BASE_URL")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    with allure.step("Open admin login page"):
        login_page.load(base_url)

    with allure.step("Login with valid admin credentials"):
        login_page.login(email, password)

    with allure.step("Verify dashboard loads successfully"):
        assert dashboard_page.dashboard_loaded()