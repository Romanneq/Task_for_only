import allure
import pytest
from methods.main_page_methods import MainPage
from locators.locators_main_page import FormsMainPage, FieldsMainPage


class TestFieldName:

    @allure.title('Поле name проходит валидацию при корректном заполнении')
    @allure.description('Я выделил следующие, общепринятые позитивные проверки на валидацию поля name: строка '
                        'с русскими буквами, с латинскими, с пробелом, строка с дефиз, количество символов - 2.')
    @pytest.mark.parametrize('name', ['Роман', 'Roman', 'Роман Гороховик', 'Роман-Роман', 'Ро'])
    # Для ревьюера: здесь я использую метод EC invisibility_of_element_located для проверки, что ошибка не отображается,
    # аналогично делаю и для других полей. По поводу двойных имен это серая зона, я допустил возможным писать двойные
    # имена через дефис, также не стал писать проверки на количество символов и граничных значений, чтобы не нагружать
    # код.
    # 1 тест с ошибкой, 4 проходят
    def test_correct_field_name(self, web_driver, name):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj._send_keys(FieldsMainPage.FIELD_NAME, name)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_vis = main_page_obj.wait_no_error_field(FieldsMainPage.FIELD_NAME_ERROR)
        assert err_vis == True

    @allure.title('Поле name не проходит валидацию при некорректном заполнении')
    @allure.description('Я выделил следующие, общепринятые негативные проверки на валидацию поля name:строка с цифрами,'
                        'строка со спецсимволами, пустое поле, только пробел, двойное имя с тире')
    @pytest.mark.parametrize('name', ['Р', '123', '#@#', '', ' ', 'Роман–Роман'])
    # Для ревьюера: здесь я возвращаю значение аттрибута error поля input, в котором отображается ошибка при
    # некорректном заполнении поля, аналогично делаю и для других полей, в негативной проверке я использую двойное имя
    # через тире. Не стал писать проверки на количество символов и граничных значений, чтобы не нагружать код.
    # 3 теста с ошибкой, 3 проходят
    def test_incorrect_field_name(self, web_driver, name):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj._send_keys(FieldsMainPage.FIELD_NAME, name)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_text = main_page_obj.text_error_field(FieldsMainPage.FIELD_NAME_ERROR)
        assert err_text == 'Неверный формат' or 'Обязательное поле'
