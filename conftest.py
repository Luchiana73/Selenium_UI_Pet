import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.enter_login()
    page.enter_password('sg2105')
    page.submit_login_button()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(ProfilePageLocators.MY_PETS_IMG_3))
    return browser
