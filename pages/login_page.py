from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def enter_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('luchiana@mail.ru')

    def enter_password(self, password):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys(password)

    def submit_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
