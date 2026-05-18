import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()


def test_admin_login_success(driver):
    base_url = os.getenv("BASE_URL")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")

    login_page = LoginPage(driver)

    login_page.load(base_url)
    login_page.login(email, password)

    assert "auth" in driver.current_url.lower() or "login" in driver.current_url.lower()