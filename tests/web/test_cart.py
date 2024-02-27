import allure
import pytest
from allure_commons.types import Severity
from selene import browser, have

from amwine_project.data import products
from amwine_project.pages.cart_page import cart_page
from amwine_project.pages.main_page import main_page


@allure.tag("web")
@allure.label("owner", "Andrey R")
@allure.feature("Cart")
class TestCart:
    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Добавление в корзину")
    def test_add_item_to_cart(self, start):
        good_old_whiskey = products.caol_ila_12
        with allure.step(f"Ищем и добавляем товар {good_old_whiskey.name} в корзину"):
            main_page.add_product_to_cart_via_search(good_old_whiskey)

        with allure.step("Проверяем, что кол-во товара в корзине увеличилось"):
            browser.element('[id="header-basket-page"]').element('.header-cart-count').should(have.exact_text('1'))

        with allure.step("Открываем страницу корзины"):
            main_page.open_cart_page()

        with allure.step(f"Проверяем, что {good_old_whiskey.name} в корзине "):
            cart_page.check_product_in_cart(good_old_whiskey)

    @allure.severity(Severity.CRITICAL)
    @allure.story("Корзина пользователя")
    @allure.title("Удаление товара из корзины")
    def test_remove_item_from_cart(self, start):
        good_whiskey = products.caol_ila_12
        with allure.step(f"Ищем и добавляем товар  {good_whiskey.name} в корзину"):
            main_page.add_product_to_cart_via_search(good_whiskey)

        with allure.step("Открываем страницу корзины"):
            main_page.open_cart_page()

        with allure.step(f"Удаляем товар {good_whiskey.name} из корзины"):
            cart_page.clear_cart()

        with allure.step("Проверяем что корзина пуста"):
            cart_page.check_cart_is_empty()
