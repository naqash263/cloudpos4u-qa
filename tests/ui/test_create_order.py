from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.config import Config


def test_create_cash_paid_order(driver):
    login_page = LoginPage(driver)
    menu_page = MenuPage(driver)

    login_page.load(Config.BASE_URL)
    login_page.login(
        Config.ADMIN_EMAIL,
        Config.ADMIN_PASSWORD
    )

    menu_page.open_pos_menu_direct(Config.BASE_URL)

    menu_page.add_first_product_to_cart()

    menu_page.place_order()

    assert menu_page.invoice_is_visible()