from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    MAIN_PAGE_LOGO = (By.CSS_SELECTOR, 'div.p-menubar-start')
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    TYPE_DOG = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="dog"]')
    TYPE_CAT = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="cat"]')
    TYPE_REPTILE = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="reptile"]')
    TYPE_HAMSTER = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="hamster"]')
    TYPE_PARROT = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="parrot"]')
    FILTER_BY_NAME = (By.ID, 'petName')
    PET_CARD = (By.CSS_SELECTOR, 'span.product-category')
    NO_RECORDS_MESSAGE = (By.CSS_SELECTOR, 'div.p-dataview-emptymessage')
    PET_DETAILS_BUTTON = (By.CSS_SELECTOR, '.p-button.p-component.p-button-raised.p-button-info.p-button-text['
                                           'aria-label="Details"]')
    ARROW_TO_NEXT_PAGE = (By.CSS_SELECTOR, 'button.p-paginator-next.p-paginator-element.p-link')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASS = (By.CSS_SELECTOR, '#password > input')
    LOGIN_BUTTON = (By.CLASS_NAME, 'p-button')
    LOGIN_MESSAGE_ERROR = (By.CSS_SELECTOR, 'div.p-message.p-component.p-message-error')


class ProfilePageLocators:
    MY_PETS_IMG_3 = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[3]/div/img')
    ADD_PET_BUTTON = (By.CSS_SELECTOR, 'span.pi.pi-plus.p-button-icon')
    DELETE_PET_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:last-child > '
                                          'div > div.product-list-action > button.p-button.p-component.p-button-danger')
    ACCEPT_DELETE_PET = (By.CSS_SELECTOR, 'button[aria-label="Yes"]')
    REJECT_DELETE_PET = (By.CSS_SELECTOR, 'button[aria-label="No"]')
    EDIT_PER_BUTTON = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-content > div > div:last-child > '
                                        'div > div.product-list-action > button:nth-child(1)')


class CreatePetPageLocators:
    PETS_NAME = (By.ID, 'name')
    PETS_AGE = (By.XPATH, '//*[@id="age"]/input')
    PET_TYPE_DROPDOWN = (By.ID, 'typeSelector')
    PET_TYPE_DOG = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="dog"]')
    PET_TYPE_CAT = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="cat"]')
    PET_TYPE_REPTILE = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="reptile"]')
    PET_TYPE_HAMSTER = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="hamster"]')
    PET_TYPE_PARROT = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="parrot"]')
    PET_GENDER_DROPDOWN = (By.ID, 'genderSelector')
    GENDER_MALE = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="Male"]')
    GENDER_FEMALE = (By.CSS_SELECTOR, '.p-dropdown-item[aria-label="Female"]')
    CREATE_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    BUTTON_UPLOAD_IMG = (By.CSS_SELECTOR, 'div.p-fileupload.p-fileupload-basic.p-component')


class EditPetPageLocators:
    EDIT_PET_SAVE_BUTTON = (By.CSS_SELECTOR, '.p-button-success[aria-label="Save"]')
