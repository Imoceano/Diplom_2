import pytest

import responses
from helpers import *


class TestCreateUser:
    @allure.title('Успешная регистрация нового пользователя.')
    def test_random_data_new_user_created(self, generate_user_and_delete):
        data = generate_user_and_delete
        response = register_user(data)
        assert (
                response.status_code == 200
                and response.json()['success'] is True
        )

    @allure.title('Регистрация пользователя, который уже существует.')
    def test_existing_user_user_already_exists(self, generate_user_register_and_delete):
        data = generate_user_register_and_delete[0]
        response = register_user(data)
        assert (
                response.status_code == 403
                and response.json()['message'] == responses.EXISTED_USER_REGISTRATION
        )

    @allure.title('Провальная регистрация пользователя при недостаточном количестве данных.')
    @pytest.mark.parametrize('data', [({'email': 'konstantin_golovin_97@ya.com',
                                        'password': 'spangebob',
                                        'name': ''}),
                                      ({'email': '',
                                        'password': 'youshallnotpassword',
                                        'name': 'Imoceano'}),
                                      ({'email': 'konstantin_golovin_97@ya.com',
                                        'password': '',
                                        'name': 'Imoceano'}),
                                      ({'email': '',
                                        'password': '',
                                        'name': ''})
                                      ])
    def test_empty_necessary_fields_not_enough_data(self, data):
        response = register_user(data)
        assert (
                response.status_code == 403
                and response.json()['message'] == responses.NOT_ENOUGH_INFO_REGISTRATION
        )
