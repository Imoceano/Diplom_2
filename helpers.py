import allure
import requests
import endpoints
from faker import Faker
import secrets

faker = Faker()

@allure.step('Генерация случайного хэша.')
def generate_random_hex_24():
    hex = secrets.token_hex(12)
    return hex


@allure.step('Генерация пользователя со случайными данными')
def generate_info_for_registration():
    info = {
        'email': faker.email(),
        'password': faker.password(),
        'name': faker.name()
    }
    return info


@allure.step('Отправка запроса на регистрацию сгенерированного пользователя.')
def register_user(payload):
    request = requests.post(f'{endpoints.URL + endpoints.CREATE_USER_HANDLER}', json=payload)
    return request


@allure.step('Отправка запроса на логин сгенерированного пользователя.')
def login_user(payload):
    request = requests.post(f'{endpoints.URL + endpoints.LOGIN_USER_HANDLER}', json=payload)
    return request


@allure.step('Отправка запроса на удаление сгенерированного пользователя.')
def delete_user(token):
    headers = {
        "Authorization": token
    }
    request = requests.delete(f'{endpoints.URL + endpoints.INFO_USER_HANDLER}', headers=headers)
    return request


@allure.step('Отправка запроса на получение информации о сгенерированном пользователе.')
def get_user_info(token):
    headers = {
        "Authorization": token
    }
    request = requests.get(f'{endpoints.URL + endpoints.INFO_USER_HANDLER}', headers=headers)
    return request


@allure.step('Отправка запроса на обновление данных о сгенерированном пользователе.')
def change_user_info(token, payload):
    headers = {
        "Authorization": token
    }
    request = requests.patch(f'{endpoints.URL + endpoints.INFO_USER_HANDLER}', headers=headers, json=payload)
    return request


@allure.step('Отправка запроса на получение данных об ингредиентах.')
def get_ingredients():
    request = requests.get(f'{endpoints.URL + endpoints.GET_INGREDIENTS_HANDLER}')
    ingredients = []
    for i in request.json()['data']:
        ingredients.append(i['_id'])
        return ingredients


@allure.step('Отправка запроса на создание заказа.')
def create_order(token, ids):
    headers = {
        "Authorization": token
    }
    payload = {
        "ingredients": ids
    }
    request = requests.post(f'{endpoints.URL + endpoints.ORDERS_HANDLER}', headers=headers, json=payload)
    return request


@allure.step('Отправка запроса на получение списка заказов.')
def get_orders_list(token):
    headers = {
        "Authorization": token
    }
    request = requests.get(f'{endpoints.URL + endpoints.ORDERS_HANDLER}', headers=headers)
    return request