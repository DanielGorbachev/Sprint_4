from selenium.webdriver.common.by import By


class MPLocator:
    order_button = [By.XPATH, "//div[contains(@class, 'Home')]/child::button"]

    q_prise_button = [By.XPATH, "//div[contains(text(),'Сколько это стоит?')]"]
    q_several_scooters_button = [By.XPATH, "//div[contains(text(),'несколько самокатов!')]"]
    q_rental_period_button = [By.XPATH, "//div[contains(text(),'время аренды?')]"]
    q_order_today_button = [By.XPATH, "//div[contains(text(),'прямо на сегодня?')]"]
    q_extend_order_or_return_button = [By.XPATH, "//div[contains(text(),'продлить заказ или вернуть самокат')]"]
    q_charger_scooter_button = [By.XPATH, "//div[contains(text(),'привозите зарядку')]"]
    q_cansel_order_button = [By.XPATH, "//div[contains(text(),'отменить заказ')]"]
    q_outside_MKAD_button = [By.XPATH, "//div[contains(text(),'за МКАДом')]"]

    a_prise = [By.XPATH, "//p[contains(text(),'400 рублей')]"]
    a_several_scooters = [By.XPATH, "//p[contains(text(),'один заказ — один самокат')]"]
    a_rental_period = [By.XPATH, "//p[contains(text(),'Отсчёт времени аренды начинается с момента')]"]
    a_order_today = [By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня')]"]
    a_extend_order_or_return = [By.XPATH, "//p[contains(text(),'всегда можно позвонить в поддержку')]"]
    a_charger_scooter = [By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой')]"]
    a_cansel_order = [By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли')]"]
    a_outside_MKAD = [By.XPATH, "//p[contains(text(),'Московской области')]"]

    sub_header_questions = [By.XPATH, "//div[contains(text(),'Вопросы о важном')]"]