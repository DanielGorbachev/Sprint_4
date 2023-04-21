from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MPLocator
from locators.base_page_locators import BPLocator


class MainPageSamokat:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(BPLocator.order_header_button))

    def click_make_order(self):
        self.driver.find_element(*MPLocator.order_button).click()

    def scroll_to_questions(self):
        element = self.driver.find_element(*MPLocator.sub_header_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_order_btn_appears(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(MPLocator.order_button))