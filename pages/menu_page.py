from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

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

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_pos_menu_direct(self, base_url):
        app_url = base_url
        self.driver.get(f"{app_url}/menu")

    def add_first_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_ADD_BUTTON)
        ).click()

    def place_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.PLACE_ORDER_BUTTON)
        ).click()

    def invoice_is_visible(self):
        invoice = self.wait.until(
            EC.visibility_of_element_located(self.INVOICE_POPUP)
        )
        return invoice.is_displayed()