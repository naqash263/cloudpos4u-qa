from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):

    FIRST_ADD_BUTTON = (
        By.XPATH,
        "(//button[contains(.,'Add')])[1]"
    )

    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Place Order')]"
    )

    INVOICE_POPUP = (
        By.XPATH,
        "//*[contains(text(),'Print Receipt') or contains(text(),'Kitchen Draft') or contains(text(),'Invoice')]"
    )

    def open_pos_menu_direct(self, base_url):
        app_url = base_url.replace("/secure-admin-login-8822", "")
        self.open_url(f"{app_url}/menu")

    def add_first_product_to_cart(self):
        self.click(self.FIRST_ADD_BUTTON)

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def invoice_is_visible(self):
        return self.is_visible(self.INVOICE_POPUP)