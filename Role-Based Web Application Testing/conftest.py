import pytest
from selenium import webdriver
import allure

@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")

    yield driver

    # Take screenshot if test failed
    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()


# Hook to detect test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)