import os
import allure
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()


@allure.feature("UI Authentication")
@allure.story("Invalid Admin Login")
@allure.severity(allure.severity_level.NORMAL)
def test_admin_login_invalid_password(driver):
    base_url = os.getenv("BASE_URL")
    email = os.getenv("ADMIN_EMAIL")
    wrong_password = "WrongPassword123!"

    login_page = LoginPage(driver)

    with allure.step("Open admin login page"):
        login_page.load(base_url)

    with allure.step("Attempt login with invalid password"):
        login_page.login(email, wrong_password)

    with allure.step("Validate error message or remain on auth page"):
        message = login_page.get_snackbar_message()

        assert (
            "Invalid" in message
            or "credentials" in message.lower()
            or "auth" in driver.current_url.lower()
            or "login" in driver.current_url.lower()
        )