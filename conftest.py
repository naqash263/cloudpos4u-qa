import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")

    prefs = {
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)

    yield driver

    if request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name
        screenshot_path = f"reports/screenshots/{test_name}_{timestamp}.png"

        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)