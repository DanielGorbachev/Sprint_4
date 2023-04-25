from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MPLocator
from pages.base_page import BasePage


class MainPageSamokat(BasePage):
    def click_make_order(self):
        self.click_element(MPLocator.order_button)

    def find_question(self, *locator):
        return self.browser.find_element(*locator)

    def click_yandex_logo(self):
        self.click_element(MPLocator.yandex_homepage_btn)

    def click_samokat_logo(self):
        self.click_element(MPLocator.samokat_homepage_btn)

    def click_make_order_header(self):
        self.click_element(MPLocator.order_header_button)

    def wait_for_load_yandex_search_btn(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MPLocator.yandex_search_btn))

    def accept_cookies(self):
        self.wait_for_cookie_notify_appears()
        self.click_element(MPLocator.accept_cookie)

    def wait_for_cookie_notify_appears(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MPLocator.accept_cookie))

    def move_to_header(self):
        self.browser.execute_script("scroll(0, 250);")