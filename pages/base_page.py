from locators.base_page_locators import BPLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_yandex_logo(self):
        self.driver.find_element(*BPLocator.yandex_homepage_btn).click()

    def click_samokat_logo(self):
        self.driver.find_element(*BPLocator.samokat_homepage_btn).click()

    def click_make_order_header(self):
        self.driver.find_element(*BPLocator.order_header_button).click()

    def click_accept_coockie(self):
        self.driver.find_element(*BPLocator.accept_cookie).click()

    def wait_for_coockie_notify_appears(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(BPLocator.accept_cookie))

    def accept_coockies(self):
        BasePage.wait_for_coockie_notify_appears(self)
        BasePage.click_accept_coockie(self)