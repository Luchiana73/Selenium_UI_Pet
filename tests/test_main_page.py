import time
import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.locators import MainPageLocators

response = requests.get('http://34.141.58.52:8080/#/')


@pytest.mark.skip
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(1)
    browser.save_screenshot('login_page.png')


def test_main_page_logo(login):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = MainPage(login, link)
    page.open()
    time.sleep(1)
    page.return_to_main_page()
    time.sleep(1)

    assert login.current_url == 'http://34.141.58.52:8080/#/'


@pytest.mark.regression
@pytest.mark.smoke
def test_filter_by_type(login):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(login, link)
    page.open()
    page.go_to_filter_by_type()
    page.select_pet_type_cat()
    time.sleep(1)
    login.save_screenshot('filter_by_type.png')

    assert response.status_code == 200


@pytest.mark.parametrize('name', ['Birillo', 'Pushkin', 'G15Y', 'Shephard'])
def test_filter_by_name(login, name):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(login, link)
    page.open()
    page.filter_by_name(name)
    time.sleep(1)

    if name in ['Birillo', 'Pushkin', 'Shephard']:
        assert login.find_element(*MainPageLocators.PET_CARD).is_displayed(), \
            f"Pet card found for valid pet name {name}"
    else:
        assert WebDriverWait(login, 10).until(
            EC.presence_of_element_located(MainPageLocators.NO_RECORDS_MESSAGE)
        ), f"Invalid pet name {name}, expected message 'No records found.'"


@pytest.mark.skip
def test_pet_details_button(login):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(login, link)
    page.open()
    page.go_to_pet_details()
    time.sleep(1)

    assert 'details' in login.current_url


@pytest.mark.regression
def test_go_to_next_page_arrow(login):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(login, link)
    page.open()
    time.sleep(1)
    page.go_to_next_page()
    time.sleep(1)

    assert response.status_code == 200
