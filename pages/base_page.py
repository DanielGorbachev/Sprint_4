from locators.base_page_locators import BPLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self):
        return self.browser.get(BPLocator.main_page_url)

    def wait_for_load_header(self):
        WebDriverWait(self.browser, 3).until(
            expected_conditions.visibility_of_element_located(BPLocator.order_header_button))

    def click_element(self, locator):               # новое
        element = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):             # новое
        element = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))
        element.send_keys(text)

    def wait_for_coockie_notify_appears(self):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(BPLocator.accept_cookie))