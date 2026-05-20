from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU_PAGE_READY = (
        By.XPATH,
        "//*[contains(.,'Menu') or contains(.,'Cart') or contains(.,'Place Order')]"
    )

    FIRST_ADD_BUTTON = (
        By.XPATH,
        "(//button[contains(normalize-space(.),'Add')])[1]"
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
        ##app_url = base_url.replace("/secure-admin-login-8822", "").rstrip("/")
        app_url = base_url
        menu_url = f"{app_url}/menu"

        self.open_url(menu_url)

        self.logger.info(f"Current URL after opening menu: {self.driver.current_url}")

        try:
            self.wait_for_visible(self.MENU_PAGE_READY)
        except TimeoutException:
            self.logger.info("Menu page did not show expected ready elements")
            self.logger.info(f"Current URL: {self.driver.current_url}")
            raise

    def add_first_product_to_cart(self):
        self.logger.info("Trying to add first product to cart")

        add_buttons = self.find_elements(self.FIRST_ADD_BUTTON)
        self.logger.info(f"Found Add buttons count: {len(add_buttons)}")

        if len(add_buttons) == 0:
            self.logger.info("No Add buttons found on menu page")
            self.logger.info(f"Current URL: {self.driver.current_url}")
            raise AssertionError("No Add buttons found on POS menu page")

        self.click(self.FIRST_ADD_BUTTON)

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)

    def invoice_is_visible(self):
        return self.is_visible(self.INVOICE_POPUP)