from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BPLocator
from locators.main_page_locators import MPLocator
from pages.base_page import BasePage


class MainPageSamokat(BasePage):
    # def __init__(self, browser):     #вставил BasePage, в нем уже есть __init__
    #     self.browser = browser

    def click_make_order(self):
        self.click_element(MPLocator.order_button)
        # self.browser.find_element(*MPLocator.order_button).click()

    def scroll_to_questions(self):
        element = self.browser.find_element(*MPLocator.sub_header_questions)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_order_btn_appears(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MPLocator.order_button))

    def find_question(self, *locator):
        return self.browser.find_element(*locator)

    def click_yandex_logo(self):
        self.click_element(MPLocator.yandex_homepage_btn)
        # self.browser.find_element(*BPLocator.yandex_homepage_btn).click()

    def click_samokat_logo(self):
        self.click_element(MPLocator.samokat_homepage_btn)
        # self.browser.find_element(*BPLocator.samokat_homepage_btn).click()

    def click_make_order_header(self):      #НОВОЕ
        self.click_element(MPLocator.order_header_button)
        # self.browser.find_element(*BPLocator.order_header_button).click()

    def wait_for_load_yandex_search_btn(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(MPLocator.yandex_search_btn))