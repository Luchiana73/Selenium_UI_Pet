from .base_page import BasePage
from pages.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def go_to_new_pet_page(self):
        self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON).click()

    def submit_delete_pet_button(self):
        self.browser.find_element(*ProfilePageLocators.DELETE_PET_BUTTON).click()

    def accept_delete_pet(self):
        self.browser.find_element(*ProfilePageLocators.ACCEPT_DELETE_PET).click()

    def reject_delete_pet(self):
        self.browser.find_element(*ProfilePageLocators.REJECT_DELETE_PET).click()

    def submit_edit_pet_button(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_PER_BUTTON).click()
