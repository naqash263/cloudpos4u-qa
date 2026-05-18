import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()


def test_admin_login_invalid_password(driver):
    base_url = os.getenv("BASE_URL")
    email = os.getenv("ADMIN_EMAIL")
    wrong_password = "WrongPassword123!"

    login_page = LoginPage(driver)

    login_page.load(base_url)
    login_page.login(email, wrong_password)

    message = login_page.get_snackbar_message()

    assert "Invalid" in message or "credentials" in message.lower()
    assert "auth" in driver.current_url.lower() or "login" in driver.current_url.lower()