from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import Locator
import random


class OrderPageSamokat:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_title(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(Locator.order_page_title))

    def set_name(self, name):
        self.driver.find_element(*Locator.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*Locator.surname_field).send_keys(surname)

    def set_adress(self, adress):
        self.driver.find_element(*Locator.address_field).send_keys(adress)

    def select_random_metro(self):
        element = self.driver.find_element(*Locator.metro_dropdown)
        element.click()
        for i in range(random.randint(1, 30)):
            element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)

    def set_telephone_nmbr(self, telephone):
        self.driver.find_element(*Locator.telephone_field).send_keys(telephone)

    def click_further(self):
        self.driver.find_element(*Locator.further_button).click()

    def wait_for_load_title2(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(Locator.order_page_header_rent))

    def select_random_date(self):
        self.driver.find_element(*Locator.when_to_order_btn).click()
        date_locator = f"//div[contains(@aria-label, '{random.randint(1, 30)}-е')]"
        self.driver.find_element(By.XPATH, date_locator).click()

    def select_rental_period(self):
        self.driver.find_element(*Locator.rental_period_dropdown).click()
        self.driver.find_element(*Locator.rental_dropdown_option).click()

    def select_color(self, color):
        if color == "black":
            self.driver.find_element(*Locator.select_color_black).click()
        elif color == "grey":
            self.driver.find_element(*Locator.select_color_grey).click()
        elif color == "black and gray":
            self.driver.find_element(*Locator.select_color_black).click()
            self.driver.find_element(*Locator.select_color_grey).click()

    def select_commentary_field(self, commentary):
        self.driver.find_element(*Locator.comments_field).send_keys(commentary)

    def click_order_btn(self):
        self.driver.find_element(*Locator.to_order_btn).click()

    def click_confirmation_btn(self):
        self.driver.find_element(*Locator.yes_btn).click()

    def header_order_is_complete_text(self):
        t = self.driver.find_element(*Locator.order_is_complete_header).text
        return t

    def click_view_order_status(self):
        self.driver.find_element(*Locator.btn_view_order_status).click()

    def cancel_order_title(self):
        x = self.driver.find_element(*Locator.cancel_order_btn).text
        return x
