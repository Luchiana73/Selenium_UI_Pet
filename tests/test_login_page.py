import pytest
from pages.login_page import LoginPage
from pages.locators import ProfilePageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.xfail
@pytest.mark.parametrize('password, screenshot', [
    ('sg2105', 'result_login_1.png'),
    ('4567LK', 'result_login_2.png'),
    ('trGU7', 'result_login_3.png')
])
def test_go_to_login(browser, password, screenshot):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_login()
    page.enter_password(password)
    page.submit_login_button()

    try:
        if password == 'sg2105':
            assert WebDriverWait(browser, 10).until(
                EC.visibility_of_element_located(ProfilePageLocators.MY_PETS_IMG_3)), \
                f"Successful login with valid password {password}"
        else:
            assert WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(LoginPageLocators.LOGIN_MESSAGE_ERROR)
            ), f"Invalid password {password}, expected error message"
    finally:
        browser.save_screenshot(screenshot)
