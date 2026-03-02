import allure
from pages.login_page import LoginPage

@allure.feature("Login Feature")
@allure.story("Valid Login")
def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    with allure.step("Enter valid username"):
        login.enter_username("tomsmith")

    with allure.step("Enter valid password"):
        login.enter_password("SuperSecretPassword!")

    with allure.step("Click login"):
        login.click_login()

    with allure.step("Verify success message"):
        message = login.get_flash_message()
        assert "You logged into a secure area!" in message