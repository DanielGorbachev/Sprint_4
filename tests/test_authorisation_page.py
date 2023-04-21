from selenium import webdriver
from pages.base_page import BasePage
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
from locators.base_page_locators import BPLocator
from faker import Faker
import random
import allure


class TestMakeOrder:
    driver = None
    fake = Faker('ru_RU')

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(BPLocator.main_page_url)

    def generate_random_name(self):
        return self.fake.first_name()

    def generate_random_surname(self):
        return self.fake.last_name()

    def generate_random_adress(self):
        s = ["Сишарп", "Сиплюсплюс", "Питон"]
        return f'ул.{random.choice(s)}, дом{random.randint(1,30)}, кв.{random.randint(1,300)}'

    def generate_random_phone_number(self):
        return f'+7{random.randint(0000000000,9999999999)}'

    def random_color_choice(self):
        colors = ["black", "gray", "black and gray"]
        return random.choice(colors)

    @allure.step("Ввод тестовых данных")
    def enter_customer_data(self):
        OrderPageSamokat.set_name(self, self.generate_random_name())
        OrderPageSamokat.set_surname(self, self.generate_random_surname())
        OrderPageSamokat.set_adress(self, self.generate_random_adress())
        OrderPageSamokat.select_random_metro(self)
        OrderPageSamokat.set_telephone_nmbr(self, self.generate_random_phone_number())
        OrderPageSamokat.click_further(self)
        OrderPageSamokat.wait_for_load_title2(self)
        OrderPageSamokat.select_random_date(self)
        OrderPageSamokat.select_rental_period(self)
        OrderPageSamokat.select_color(self, self.random_color_choice())
        OrderPageSamokat.select_commentary_field(self, "Комментариев никаких нет")
        OrderPageSamokat.click_order_btn(self)
        OrderPageSamokat.click_confirmation_btn(self)

    @allure.title("Проверка оформления заказа через кнопку на главной странице ")
    @allure.description(
        "Принимаем куки, нажимаем на копку заказа, вводим тестовые данные, проверяем что заказ оформлен")
    @allure.step("Переход на страницу оформления заказа")
    def test_make_order_positive_result(self):
        BasePage.accept_coockies(self)
        MainPageSamokat.click_make_order(self)
        OrderPageSamokat.wait_for_load_title(self)
        self.enter_customer_data()
        OrderPageSamokat.click_view_order_status(self)
        element = OrderPageSamokat.cancel_order_title(self)
        assert element is not None, "There was an error while checkout the order"

    @allure.title("Проверка оформления заказа через кнопку в header'е ")
    @allure.description("Принимаем куки, нажимаем на копку заказа в header'е, вводим тестовые данные, проверяем что заказ оформлен")
    @allure.step("Переход на страницу оформления заказа")
    def test_make_order_from_header_positive_result(self):
        BasePage.click_make_order_header(self)
        OrderPageSamokat.wait_for_load_title(self)
        self.enter_customer_data()
        element = OrderPageSamokat.header_order_is_complete_text(self)
        assert "Заказ оформлен" in element, "There was an error while checkout the order"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
