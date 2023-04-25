from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MPLocator
from pages.base_page import BasePage
import allure


class MainPageSamokat(BasePage):
    @allure.step("Клик по кнопке 'заказать'")
    def click_make_order(self):
        self.click_element(MPLocator.order_button)

    @allure.step("Поиск элемента по локатору")
    def find_question(self, *locator):
        return self.browser.find_element(*locator)

    @allure.step("Клик по логотипу Яндекс")
    def click_yandex_logo(self):
        self.click_element(MPLocator.yandex_homepage_btn)

    @allure.step("Клик по логотипу Самокат")
    def click_samokat_logo(self):
        self.click_element(MPLocator.samokat_homepage_btn)

    @allure.step("Клик по кнопке заказать в header'е")
    def click_make_order_header(self):
        self.click_element(MPLocator.order_header_button)

    @allure.step("Ожидание загрузки страницы Яндекса")
    def wait_for_load_yandex_search_btn(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MPLocator.yandex_search_btn))

    @allure.step("Нажатие на кнопку принятия куки")
    def accept_cookies(self):
        self.wait_for_cookie_notify_appears()
        self.click_element(MPLocator.accept_cookie)

    @allure.step("Ожидание появления окна уведомления с куками")
    def wait_for_cookie_notify_appears(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MPLocator.accept_cookie))

    @allure.step("Скрол страницы до самого верха")
    def move_to_header(self):
        self.browser.execute_script("scroll(0, 250);")