from selenium.webdriver.common.by import By


class BPLocator:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"
    yandex_homepage_btn = [By.XPATH, "//a[@rel='noopener noreferrer']"]
    samokat_homepage_btn = [By.XPATH, "//a[contains(@class, 'LogoScooter')]"]
    order_header_button = [By.XPATH, "//div[contains(@class, 'Header')]//button[contains(text(),'Заказать')]"]
    accept_cookie = [By.XPATH, "//button[@id='rcc-confirm-button']"]