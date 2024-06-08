import pytest
import allure
from helpers import *

@allure.step('Создание пользователя, передаем его данные, и затем удаляем его.')
@pytest.fixture
def generate_user_and_delete():
    payload = generate_info_for_registration()
    yield payload

    login_response = login_user(payload)
    if login_response.status_code == 200 and 'accessToken' in login_response.json():
        token = login_response.json()['accessToken']
        delete_user(token)
    else:
        print(f"Failed to log in user during teardown: {login_response.json()}")


@allure.step('Создание пользователя, регистрируем его, затем удаляем его.')
@pytest.fixture
def generate_user_register_and_delete():
    payload = generate_info_for_registration()
    register_response = register_user(payload)
    
    if register_response.status_code != 200:
        pytest.fail(f"Failed to register user: {register_response.json()}")

    login_response = login_user(payload)
    if login_response.status_code != 200 or 'accessToken' not in login_response.json():
        pytest.fail(f"Failed to log in user: {login_response.json()}")

    token = login_response.json()['accessToken']
    yield payload, token

    delete_user(token)
