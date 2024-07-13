import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseMethods:  # создали класс базовых методов selenium
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Метод скролла страницы')
    def base_scroll_page(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Метод явного ожидания отображения элемента')
    def wait_element_page(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Метод ожидания отсутствия элемента')
    def re_wait_element_page(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Метод получения текста ошибки')
    def base_text_error(self, locator):
        return self.driver.find_element(*locator).get_attribute("error")

    @allure.step('Метод клика по элементу страницы')
    def click_element_page(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Метод ввода текста в поле элемента страницы')
    def send_keys_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)
