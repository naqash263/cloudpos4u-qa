from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_ELEMENT = (
        By.XPATH,
        "//*[contains(text(),'Good Afternoon') or contains(text(),'Completed Orders') or contains(text(),'Sales')]"
    )

    def dashboard_loaded(self):
        return self.is_visible(self.DASHBOARD_ELEMENT)