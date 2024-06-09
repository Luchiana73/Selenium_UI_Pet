import time
import pytest
from pages.profile_page import ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import EditPetPageLocators


@pytest.mark.skip
def test_button_create_new_pet(login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(login, link)
    page.open()
    page.go_to_new_pet_page()
    time.sleep(2)

    assert login.current_url.endswith('pet-new/pet')


@pytest.mark.smoke
def test_button_delete_pet(login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(login, link)
    page.open()
    page.submit_delete_pet_button()
    time.sleep(1)
    page.accept_delete_pet()
    time.sleep(1)


def test_button_edit_pet(login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(login, link)
    page.open()
    page.submit_edit_pet_button()
    time.sleep(2)

    assert WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(EditPetPageLocators.EDIT_PET_SAVE_BUTTON))
