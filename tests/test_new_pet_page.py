import pytest
from pages.new_pet_page import CreateNewPet
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import CreatePetPageLocators


@pytest.mark.smoke
def test_create_pet(login):
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = CreateNewPet(login, link)
    page.open()
    page.enter_pet_name()
    page.enter_pet_age()
    page.go_to_pet_type_selection()
    page.select_pet_type_parrot()
    page.go_to_pet_gender_selection()
    page.select_pet_gender_male()
    page.submit_create_pet_button()

    login.save_screenshot('create_pet.png')

    assert WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(CreatePetPageLocators.BUTTON_UPLOAD_IMG))
