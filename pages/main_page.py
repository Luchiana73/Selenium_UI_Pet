from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def return_to_main_page(self):
        self.browser.find_element(*MainPageLocators.MAIN_PAGE_LOGO).click()

    def go_to_filter_by_type(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE).click()

    def select_pet_type_cat(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.TYPE_CAT)).click()

    def filter_by_name(self, name):
        input_field = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        input_field.send_keys(name)
        input_field.send_keys(Keys.ENTER)

    def go_to_pet_details(self):
        self.browser.find_element(*MainPageLocators.PET_DETAILS_BUTTON).click()

    def go_to_next_page(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ARROW_TO_NEXT_PAGE)).click()
