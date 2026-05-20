import allure
from pages import dashboard_page
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.config import Config


@allure.feature("UI POS Order Management")
@allure.story("Create Cash Paid Order")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_cash_paid_order(driver):
    login_page = LoginPage(driver)
    menu_page = MenuPage(driver)

    with allure.step("Open admin login page"):
        login_page.load(Config.BASE_URL)

    with allure.step("Login with valid admin credentials"):
        login_page.login(
            Config.ADMIN_EMAIL,
            Config.ADMIN_PASSWORD
        )

    with allure.step("Open POS menu page"):
        menu_page.open_pos_menu_direct(Config.BASE_URL)

    with allure.step("Wait until menu page is visible"):
        menu_page.wait_for_visible(menu_page.FIRST_ADD_BUTTON)

    with allure.step("Add first available product to cart"):
        menu_page.add_first_product_to_cart()

    with allure.step("Place cash paid order"):
        menu_page.place_order()

    with allure.step("Verify invoice is visible"):
        assert menu_page.invoice_is_visible()