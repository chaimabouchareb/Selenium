from pages.login_page import LoginPage

def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.enter_username("wrong")
    login.enter_password("wrong")
    login.click_login()

    message = login.get_flash_message()
    assert "Your username is invalid!" in message