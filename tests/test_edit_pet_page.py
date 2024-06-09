import time
import pytest
from pages.edit_pet_page import EditPet


@pytest.mark.parametrize('pet_id', [27197, 27199, 27200])
def test_edit_pet_save_button(login, pet_id):
    link = f'http://34.141.58.52:8080/#/pet-edit/{pet_id}'
    page = EditPet(login, link)
    page.open()
    time.sleep(1)
    page.submit_edit_pet_save_button()
    time.sleep(1)

    assert login.current_url.endswith('message=Your+pet+has+been+successfully+saved')
