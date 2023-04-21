# Проект автоматизации тестирования сайта "СамокатЯндекс"
1. Основа для написания автотестов — фреймворк pytest, selenium
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v. 


Описаний файлов тестов:
- test_main_page:
  - test_dropdown_answer_{number}_appears
    - проверка работоспособности выпадающих ответов на вопросы, и их соответствие 
  - test_return_to_main_page_from_header_positive_result
    - проверка открытия главной страницы сайта посредством нажатия на логотип в header'е
  - test_yandex_open_new_page_positive_result
    - проверка перехода на главную страницу Яндекса посредством нажатия на логотип в header'е
- test_authorisation_page
  - test_make_order_positive_result
    - полный позитивный сценарий заказа самоката с помощью кнопки на главной странице
  - test_make_order_from_header_positive_result
    - полный позитивный сценарий заказа самоката с помощью кнопки в header'е
  