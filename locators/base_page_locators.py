from selenium.webdriver.common.by import By


class BPLocator:
    main_page_url = "https://qa-scooter.praktikum-services.ru/"

    accept_cookie = [By.XPATH, "//button[@id='rcc-confirm-button']"]