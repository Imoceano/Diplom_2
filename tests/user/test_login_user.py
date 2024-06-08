import responses
from helpers import *


class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя.')
    def test_correct_user_successful_login(self, generate_user_register_and_delete):
        data = generate_user_register_and_delete[0]
        response = login_user(data)
        assert (
                response.status_code == 200
                and response.json()['success'] is True
        )

    @allure.title('Проверка провальной авторизации пользователя.')
    def test_incorrect_email_unauthorized(self, generate_user_and_delete):
        data = generate_user_and_delete
        response = login_user(data)
        assert (
                response.status_code == 401
                and response.json()['message'] == responses.INCORRECT_INFO_LOGIN
        )