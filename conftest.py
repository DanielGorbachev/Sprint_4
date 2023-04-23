import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BPLocator
from pages.base_page import BasePage


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    driver.get(BPLocator.main_page_url)
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(BPLocator.order_header_button))
    yield driver
    driver.quit()

@pytest.fixture
def accept_coockies(self):
    BasePage.wait_for_coockie_notify_appears(self)
    BasePage.click_element(BPLocator.accept_cookie)