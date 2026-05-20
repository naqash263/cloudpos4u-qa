from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def open_url(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def wait_for_visible(self, locator):
        self.logger.info(f"Waiting for element visible: {locator}")
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        self.logger.info(f"Waiting for element clickable: {locator}")
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        self.wait_for_clickable(locator).click()

    def type_text(self, locator, text):
        self.logger.info(f"Typing text into element: {locator}")
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")
        return self.wait_for_visible(locator).text.strip()

    def get_text_content(self, locator):
        self.logger.info(f"Getting textContent from element: {locator}")
        element = self.wait_for_visible(locator)

        text = element.text.strip()

        if not text:
            text = element.get_attribute("textContent").strip()

        return text

    def is_visible(self, locator):
        self.logger.info(f"Checking element visibility: {locator}")
        return self.wait_for_visible(locator).is_displayed()

    def current_url_contains(self, text):
        self.logger.info(f"Checking current URL contains: {text}")
        return text.lower() in self.driver.current_url.lower()

    def wait_for_url_contains(self, text):
        self.logger.info(f"Waiting for URL to contain: {text}")
        return self.wait.until(
            lambda driver: text.lower() in driver.current_url.lower()
        )

    def wait_for_url_not_contains(self, text):
        self.logger.info(f"Waiting for URL to not contain: {text}")
        return self.wait.until(
            lambda driver: text.lower() not in driver.current_url.lower()
        )
    def find_elements(self, locator):
        self.logger.info(f"Finding elements: {locator}")

        return self.driver.find_elements(*locator)

    def page_contains_text(self, text):
        return text.lower() in self.driver.page_source.lower()