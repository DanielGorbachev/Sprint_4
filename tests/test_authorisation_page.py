from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
import allure


class TestMakeOrder:
    @allure.title("Проверка оформления заказа через кнопку на главной странице ")
    @allure.description(
        "Принимаем куки, нажимаем на копку заказа, вводим тестовые данные, проверяем что заказ оформлен")
    @allure.step("Переход на страницу оформления заказа")
    def test_make_order_positive_result(self, browser):
        main_page = MainPageSamokat(browser)
        order_page = OrderPageSamokat(browser)
        main_page.accept_cookies()
        main_page.click_make_order()
        order_page.wait_for_load_title()
        order_page.enter_customer_data()
        order_page.click_view_order_status()
        element = order_page.cancel_order_title()
        assert element is not None, "There was an error while checkout the order"

    @allure.title("Проверка оформления заказа через кнопку в header'е ")
    @allure.description("Принимаем куки, нажимаем на копку заказа в header'е, вводим тестовые данные, проверяем что заказ оформлен")
    @allure.step("Переход на страницу оформления заказа")
    def test_make_order_from_header_positive_result(self, browser):
        main_page = MainPageSamokat(browser)
        order_page = OrderPageSamokat(browser)
        main_page.click_make_order_header()
        order_page.wait_for_load_title()
        order_page.enter_customer_data()
        element = order_page.header_order_is_complete_text()
        assert "Заказ оформлен" in element, "There was an error while checkout the order"