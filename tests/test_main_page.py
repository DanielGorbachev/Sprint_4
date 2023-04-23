from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MPLocator
from pages.base_page import BasePage
from pages.main_page import MainPageSamokat
from locators.base_page_locators import BPLocator
import allure
import pytest


class TestMainPageQuestions:

    answers = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]
    @allure.title("Проверка появления ответов при нажатии на вопросы на главной странице")
    @allure.description('На странице ищем элемент c вопросом и проверяем его ответ')
    @pytest.mark.parametrize("question,answer,expected_answer", [
        [MPLocator.q_prise_button, MPLocator.a_prise, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
        [MPLocator.q_several_scooters_button, MPLocator.a_several_scooters,
         "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
        [MPLocator.q_rental_period_button, MPLocator.a_rental_period,
         "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
        [MPLocator.q_order_today_button, MPLocator.a_order_today, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
        [MPLocator.q_extend_order_or_return_button,MPLocator.a_extend_order_or_return,
         "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
        [MPLocator.q_charger_scooter_button,MPLocator.a_charger_scooter,
         "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
        [MPLocator.q_cansel_order_button, MPLocator.a_cansel_order,
         "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
        [MPLocator.q_outside_MKAD_button, MPLocator.a_outside_MKAD, "Да, обязательно. Всем самокатов! И Москве, и Московской области."]
    ])
    def test_dropdown_questions_answer_appears(self, browser, question, answer, expected_answer):
        main_page = MainPageSamokat(browser)
        main_page.scroll_to_questions()
        question_element = main_page.find_question(*question)
        question_element.click()
        answer = main_page.find_question(*answer).text
        assert answer == expected_answer, f"Answer doesn't match for question '{question}'"


class TestLogoNavigation:
    @allure.title("Возврат на главную страницу сайта при нажатии на логотип самоката")
    @allure.description('Переходим на страницу с оформлением заказа и возвращаемся с нее на главную страницу сайта')
    def test_return_to_main_page_from_header_positive_result(self, browser):
        main_page = MainPageSamokat(browser)
        main_page.move_to_header()
        main_page.click_make_order_header()
        main_page.click_samokat_logo()
        element = browser.current_url
        site_url = BPLocator.main_page_url
        assert element == site_url

    @allure.title("Нажатие на логотип 'Яндекс' открывает главную страницу Яндекса")
    def test_yandex_open_new_page_positive_result(self, browser):
        main_page = MainPageSamokat(browser)
        main_page.click_yandex_logo()
        browser.switch_to.window(browser.window_handles[1])
        main_page.wait_for_load_yandex_search_btn()
        site_url = browser.current_url
        assert "dzen.ru" in site_url, "Error when trying to go to the main page of Yandex"