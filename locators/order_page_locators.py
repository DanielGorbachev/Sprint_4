from selenium.webdriver.common.by import By


class Locator:
    order_page_title = [By.XPATH, "//div[contains(text(),'Для кого самокат')]"]
    name_field = [By.XPATH, "//input[contains(@placeholder, 'Имя')]"]
    surname_field = [By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"]
    address_field = [By.XPATH, "//input[contains(@placeholder, 'Адрес')]"]
    metro_dropdown = [By.XPATH, "//input[contains(@placeholder, 'метро')]"]
    telephone_field = [By.XPATH, "//input[contains(@placeholder, 'Телефон')]"]

    further_button = [By.XPATH, "//button[contains(text(),'Далее')]"]

    order_page_header_rent = [By.XPATH, "//div[contains(text(),'Про аренду')]"]
    when_to_order_btn = [By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]"]

    rental_period_dropdown = [By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]"]
    rental_dropdown_option = [By.XPATH, "//div[contains(text(),'сутки')]"]
    select_color_black = [By.XPATH, "//input[@id='black']"]
    select_color_grey = [By.XPATH, "//input[@id='grey']"]
    comments_field = [By.XPATH, "//input[contains(@placeholder, 'Комментарий')]"]

    to_order_btn = [By.XPATH, "//div[contains(@class, 'Order')]//button[contains(text(),'Заказать')]"]
    back_btn = [By.XPATH, "//button[contains(text(),'Назад')]"]

    confirm_header = [By.XPATH, "//div[contains(text(),'Хотите оформить заказ?')]"]

    yes_btn = [By.XPATH, "//button[contains(text(),'Да')]"]
    no_btn = [By.XPATH, "//button[contains(text(),'Нет')]"]

    order_is_complete_header = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]
    btn_view_order_status = [By.XPATH, "//button[contains(text(),'Посмотреть статус')]"]
    cancel_order_btn = [By.XPATH, "//button[contains(text(),'Отменить заказ')]"]
