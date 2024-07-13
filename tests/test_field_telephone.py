import allure
import pytest
from methods.main_page_methods import MainPage
from locators.locators_main_page import FormsMainPage, FieldsMainPage


class TestFieldTelephone:

    @allure.title('Поле telephone проходит валидацию при корректном заполнении')
    @allure.description('Я выделил следующие, общепринятые позитивные проверки на валидацию поля telephone:'
                        'Только цифры с количеством символов - 10')
    # Для ревьюера: assert аналогичен в тесте на поле name
    # тест проходит
    def test_correct_field_telephone(self, web_driver):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.click_elem_main_page(FieldsMainPage.FIELD_TEL)
        main_page_obj._send_keys(FieldsMainPage.FIELD_TEL, 9963147119)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_vis = main_page_obj.wait_no_error_field(FieldsMainPage.FIELD_TEL_ERROR)
        assert err_vis == True

    @allure.title('Поле telephone не проходит валидацию при некорректном заполнении')
    @allure.description('Я выделил следующие, общепринятые негативные проверки на валидацию поля telephone: '
                        'количество символов <  10, только буквы, только спецсимволы')
    @pytest.mark.parametrize('tel', ['5555555', 'абвгдейка', '@##@'])
    # Для ревьюера: assert аналогичен в тесте на поле name
    # тесты проходят
    def test_incorrect_field_telephone(self, web_driver, tel):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.click_elem_main_page(FieldsMainPage.FIELD_TEL)
        main_page_obj._send_keys(FieldsMainPage.FIELD_TEL, tel)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_text = main_page_obj.text_error_field(FieldsMainPage.FIELD_TEL_ERROR)
        assert err_text == 'Неверный формат' or 'Обязательное поле'

    @allure.title('Можно поменять код страны в поле telephone')
    # Для ревьюера: кликаю на флаг в поле telephone, выбираю страну Беларусь, проверяю, что страна отобразилась
    # в поле telephone
    # тест проходит
    def test_success_change_country(self, web_driver):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.click_elem_main_page(FieldsMainPage.FLAG_TEL)
        main_page_obj.click_elem_main_page(FieldsMainPage.COUNTRY_BEL)
        assert main_page_obj.wait_main_page(FieldsMainPage.BEL_TEL)
