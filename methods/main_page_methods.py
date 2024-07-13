import allure
from methods.base_methods import BaseMethods


class MainPage(BaseMethods):  # Создали класс главной страницы cервиса

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения главной страницы сервиса')
    def wait_main_page(self: BaseMethods, locator):
        return self.wait_element_page(locator)

    @allure.step('Метод заполнения поля')
    def _send_keys(self: BaseMethods, locator, text_name):
        self.send_keys_element(locator, text_name)

    @allure.step('Метод ожидания отсутствия ошибки в поле')
    def wait_no_error_field(self: BaseMethods, locator):
        return self.re_wait_element_page(locator)

    @allure.step('Метод получения текста ошибки поля')
    def text_error_field(self: BaseMethods, locator):
        return self.base_text_error(locator)

    @allure.step('Метод скролла страницы')
    def scroll_page(self: BaseMethods, locator):
        self.base_scroll_page(locator)

    @allure.step('Метод клика по элементу главной страницы')
    def click_elem_main_page(self: BaseMethods, elem):
        self.click_element_page(elem)
