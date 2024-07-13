import allure
from methods.base_methods import BaseMethods


class OfficialPage(BaseMethods):  # Создали класс главной страницы cервиса

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод отображения официальной страницы Only')
    def wait_official_page(self: BaseMethods, locator):
        return self.wait_element_page(locator)
