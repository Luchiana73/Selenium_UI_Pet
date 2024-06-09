from .base_page import BasePage
from pages.locators import CreatePetPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateNewPet(BasePage):
    def enter_pet_name(self):
        self.browser.find_element(*CreatePetPageLocators.PETS_NAME).send_keys('Rif')

    def enter_pet_age(self):
        self.browser.find_element(*CreatePetPageLocators.PETS_AGE).send_keys('3')

    def go_to_pet_type_selection(self):
        self.browser.find_element(*CreatePetPageLocators.PET_TYPE_DROPDOWN).click()

    def select_pet_type_parrot(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(CreatePetPageLocators.PET_TYPE_PARROT)).click()

    def go_to_pet_gender_selection(self):
        self.browser.find_element(*CreatePetPageLocators.PET_GENDER_DROPDOWN).click()

    def select_pet_gender_male(self):
        self.browser.find_element(*CreatePetPageLocators.GENDER_MALE).click()

    def submit_create_pet_button(self):
        self.browser.find_element(*CreatePetPageLocators.CREATE_PET_BUTTON).click()
