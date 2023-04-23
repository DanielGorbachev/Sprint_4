from locators.base_page_locators import BPLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MPLocator


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self):
        return self.browser.get(BPLocator.main_page_url)

    def wait_for_load_header(self):
        WebDriverWait(self.browser, 3).until(
            expected_conditions.visibility_of_element_located(MPLocator.order_header_button))

    def click_element(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        element.click()