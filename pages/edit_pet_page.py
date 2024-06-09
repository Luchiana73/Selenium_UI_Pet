from .base_page import BasePage
from pages.locators import EditPetPageLocators


class EditPet(BasePage):

    def submit_edit_pet_save_button(self):
        self.browser.find_element(*EditPetPageLocators.EDIT_PET_SAVE_BUTTON).click()
