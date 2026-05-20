from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_ELEMENT = (
        By.XPATH,
        "//*[contains(text(),'Good Afternoon') or contains(text(),'Total Revenue') or contains(text(),'Revenue Overview')]"
    )

    def dashboard_loaded(self):
        return self.is_visible(self.DASHBOARD_ELEMENT)