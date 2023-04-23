from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import Locator
import random
from pages.base_page import BasePage
from faker import Faker
import allure


class OrderPageSamokat(BasePage):
    fake = Faker('ru_RU')
    def wait_for_load_title(self):
        WebDriverWait(self.browser, 3).until(expected_conditions.visibility_of_element_located(Locator.order_page_title))

    def set_name(self, name):
        self.browser.find_element(*Locator.name_field).send_keys(name)

    def set_surname(self, surname):
        self.browser.find_element(*Locator.surname_field).send_keys(surname)

    def set_adress(self, adress):
        self.browser.find_element(*Locator.address_field).send_keys(adress)

    def select_random_metro(self):
        element = self.browser.find_element(*Locator.metro_dropdown)
        element.click()
        for i in range(random.randint(1, 30)):
            element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def set_telephone_nmbr(self, telephone):
        self.browser.find_element(*Locator.telephone_field).send_keys(telephone)

    def click_further(self):
        self.click_element(Locator.further_button)

    def wait_for_load_title2(self):
        WebDriverWait(self.browser, 3).until(expected_conditions.visibility_of_element_located(Locator.order_page_header_rent))

    def select_random_date(self):
        self.click_element(Locator.when_to_order_btn)
        date_locator = f"//div[contains(@aria-label, '{random.randint(1, 30)}-е')]"
        self.browser.find_element(By.XPATH, date_locator).click()

    def select_rental_period(self):
        self.click_element(Locator.rental_period_dropdown)
        self.click_element(Locator.rental_dropdown_option)

    def select_color(self, color):
        if color == "black":
            self.click_element(Locator.select_color_black)
        elif color == "grey":
            self.click_element(Locator.select_color_grey)
        elif color == "black and gray":
            self.click_element(Locator.select_color_black)
            self.click_element(Locator.select_color_grey)

    def select_commentary_field(self, commentary):
        self.browser.find_element(*Locator.comments_field).send_keys(commentary)

    def click_order_btn(self):
        self.click_element(Locator.to_order_btn)

    def click_confirmation_btn(self):
        self.click_element(Locator.yes_btn)

    def header_order_is_complete_text(self):
        order_complete_text = self.browser.find_element(*Locator.order_is_complete_header).text
        return order_complete_text

    def click_view_order_status(self):
        self.click_element(Locator.btn_view_order_status)

    def cancel_order_title(self):
        cancel_order_text = self.browser.find_element(*Locator.cancel_order_btn).text
        return cancel_order_text

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
        OrderPageSamokat.set_name(self,self.generate_random_name())
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