from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (
        By.XPATH,
        "//span[contains(normalize-space(),'Log In')]/ancestor::button"
    )

    SNACKBAR_MESSAGE = (
        By.CSS_SELECTOR,
        ".SnackbarContent-root, .notistack-Snackbar, [role='alert']"
    )

    def load(self, url):
        self.open_url(url)

    def enter_email(self, email):
        self.type_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_snackbar_message(self):
        return self.get_text_content(self.SNACKBAR_MESSAGE)