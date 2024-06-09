import pytest

import responses
from helpers import *


class TestChangeUser:
    @allure.title('Успешное редактирование пользователя.')
   
    @pytest.mark.parametrize('update_data', [({'email': faker.email()}),
                                      ({'password': faker.password()}),
                                      ({'name': faker.name()})])
    def test_authorized_user_successful_change(self, generate_user_register_and_delete, update_data):
        token = generate_user_register_and_delete[1]
        change_response = change_user_info(token, update_data)
        assert (
                change_response.status_code == 200
                and change_response.json()['success'] is True
        )

    @allure.title('Возврат ошибки при попытке сохранения изменений для редактируемого пользователя.')
    @pytest.mark.parametrize('update_data', [({'email': faker.email()}),
                                             ({'password': faker.password()}),
                                             ({'name': faker.name()})])
    def test_not_authorized_user_unauthorized_error(self, update_data):
        change_response = change_user_info(token='Unauthorized', payload=update_data)
        assert (
                change_response.status_code == 401
                and change_response.json()['message'] == responses.NO_AUTHORIZED
        )