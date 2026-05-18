from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    DASHBOARD_ELEMENT = (
        By.XPATH,
        "//*[contains(text(),'Good Afternoon') or contains(text(),'Completed Orders') or contains(text(),'Sales')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def dashboard_loaded(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_ELEMENT)
        )
        return element.is_displayed()