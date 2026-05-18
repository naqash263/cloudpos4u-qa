from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON = (
        By.XPATH,
        "//span[contains(normalize-space(),'Log In')]/ancestor::button"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def load(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        ).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_snackbar_message(self):
        snackbar = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    ".SnackbarContent-root, .notistack-Snackbar, [role='alert']"
                )
            )
        )
        return snackbar.text

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()