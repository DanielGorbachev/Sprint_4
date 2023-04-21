from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MPLocator
from pages.base_page import BasePage
from pages.main_page import MainPageSamokat
from locators.base_page_locators import BPLocator
import allure


class TestMainPageQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(BPLocator.main_page_url)

    @allure.title("Проверка появления ответов при нажатии на вопросы на главной странице")
    @allure.description('На странице ищем элемент c вопросом и проверяем его ответ')
    @allure.step("Ответ на вопрос №1")
    def test_dropdown_answer_1_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_prise_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(MPLocator.a_prise))
        answer = self.driver.find_element(*MPLocator.a_prise).text
        assert answer == expected_answers["expected_answer1"], f"Answer doesn't match for question '{MPLocator.q_prise_button}'"

    @allure.step("Ответ на вопрос №2")
    def test_dropdown_answer_2_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_several_scooters_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_several_scooters))
        answer = self.driver.find_element(*MPLocator.a_several_scooters).text
        assert answer == expected_answers["expected_answer2"], f"Answer doesn't match for question '{MPLocator.q_several_scooters_button}'"

    @allure.step("Ответ на вопрос №3")
    def test_dropdown_answer_3_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_rental_period_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_rental_period))
        answer = self.driver.find_element(*MPLocator.a_rental_period).text
        assert answer == expected_answers[
            "expected_answer3"], f"Answer doesn't match for question '{MPLocator.q_rental_period_button}'"

    @allure.step("Ответ на вопрос №4")
    def test_dropdown_answer_4_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_order_today_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_order_today))
        answer = self.driver.find_element(*MPLocator.a_order_today).text
        assert answer == expected_answers[
            "expected_answer4"], f"Answer doesn't match for question '{MPLocator.q_order_today_button}'"

    @allure.step("Ответ на вопрос №5")
    def test_dropdown_answer_5_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_extend_order_or_return_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_extend_order_or_return))
        answer = self.driver.find_element(*MPLocator.a_extend_order_or_return).text
        assert answer == expected_answers[
            "expected_answer5"], f"Answer doesn't match for question '{MPLocator.q_extend_order_or_return_button}'"

    @allure.step("Ответ на вопрос №6")
    def test_dropdown_answer_6_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_charger_scooter_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_charger_scooter))
        answer = self.driver.find_element(*MPLocator.a_charger_scooter).text
        assert answer == expected_answers[
            "expected_answer6"], f"Answer doesn't match for question '{MPLocator.q_charger_scooter_button}'"

    @allure.step("Ответ на вопрос №7")
    def test_dropdown_answer_7_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_cansel_order_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_cansel_order))
        answer = self.driver.find_element(*MPLocator.a_cansel_order).text
        assert answer == expected_answers[
            "expected_answer7"], f"Answer doesn't match for question '{MPLocator.q_cansel_order_button}'"

    @allure.step("Ответ на вопрос №8")
    def test_dropdown_answer_8_appears(self, expected_answers):
        MainPageSamokat.scroll_to_questions(self)
        question = self.driver.find_element(*MPLocator.q_outside_MKAD_button)
        question.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(MPLocator.a_outside_MKAD))
        answer = self.driver.find_element(*MPLocator.a_outside_MKAD).text
        assert answer == expected_answers[
            "expected_answer8"], f"Answer doesn't match for question '{MPLocator.q_outside_MKAD_button}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


class TestLogoNavigation:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(BPLocator.main_page_url)

    @allure.title("Возврат на главную страницу сайта при нажатии на логотип самоката")
    @allure.description('Переходим на страницу с оформлением заказа и возвращаемся с нее на главную страницу сайта')
    def test_return_to_main_page_from_header_positive_result(self):
        BasePage.click_make_order_header(self)
        BasePage.click_samokat_logo(self)
        element = self.driver.current_url
        site_url = BPLocator.main_page_url
        assert element == site_url

    @allure.title("Нажатие на логотип 'Яндекс' открывает главную страницу Яндекса")
    def test_yandex_open_new_page_positive_result(self):
        BasePage.click_yandex_logo(self)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Найти')]")))
        element = self.driver.find_element(By.XPATH, "//div[contains(text(),'Поиск Яндекса')]").text
        assert element is not None, "Error when trying to go to the main page of Yandex"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()