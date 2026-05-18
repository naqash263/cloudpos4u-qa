import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

load_dotenv()


def test_dashboard_load_after_login(driver):
    base_url = os.getenv("BASE_URL")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.load(base_url)
    login_page.login(email, password)

    assert dashboard_page.dashboard_loaded()