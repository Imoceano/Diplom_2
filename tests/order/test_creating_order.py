import responses
from helpers import *


class TestCreateOrder:
    @allure.title('Ошибка при создании заказа без ингредиентов.')
    def test_unauthorized_user_without_ingredients_no_ingredients_error(self):
        order_response = create_order(token='Unauthorized', ids=None)
        assert (
                order_response.status_code == 400
                and order_response.json()['message'] == responses.NO_INGREDIENTS
        )
    @allure.title('Успешное создание заказа с ингредиентами.')
    def test_unauthorized_user_with_ingredients_order_created(self):
        ingredients = get_ingredients()
        order_response = create_order(token='Unauthorized', ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
            )

    @allure.title('Ошибка при создании заказа без ингредиентов для авторизованного пользователя.')
    def test_authorized_user_without_ingredients_no_ingredients_error(self, generate_user_register_and_delete):
        token = generate_user_register_and_delete[1]
        order_response = create_order(token=token, ids=None)
        assert (
                order_response.status_code == 400
                and order_response.json()['message'] == responses.NO_INGREDIENTS
        )

    @allure.title('Успешное создание заказа с ингредиентами для авторизованного пользователя.')
    def test_authorized_user_with_ingredients_order_created(self, generate_user_register_and_delete):
        token = generate_user_register_and_delete[1]
        ingredients = get_ingredients()
        order_response = create_order(token=token, ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
        )

    @allure.title('Ошибка при создании заказа с неверным хешем ингредиентов для авторизованного пользователя.')
    def test_authorized_user_with_incorrect_hex_order_created(self, generate_user_register_and_delete):
        token = generate_user_register_and_delete[1]
        ingredients = generate_random_hex_24()
        order_response = create_order(token=token, ids=ingredients)
        assert (
                order_response.status_code == 400
                and order_response.json()['message'] == responses.INCORRECT_INGREDIENT
        )
