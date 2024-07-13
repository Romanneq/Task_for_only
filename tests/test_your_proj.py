import allure
import pytest
from methods.main_page_methods import MainPage
from locators.locators_main_page import FormsMainPage, FieldsMainPage


class TestYourProject:

    @allure.title('Поле your proj проходит валидацию при корректном заполнении')
    @allure.description('Я выделил следующие позитивные проверки на валидацию поля your proj:'
                        'Количество символов = 1, 999, 1000, 555, спецсимволы нельзя вводить')
    @pytest.mark.parametrize('quantity, symbol', [['1', 's'], ['999', 's'], ['1000', 's'], ['555', 's'], ['1', '*']])
    # тест проходит
    def test_correct_field_your_proj(self, web_driver, quantity, symbol):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.scroll_page(FormsMainPage.FORM_ABOUT_COMPANY)
        main_page_obj._send_keys(FieldsMainPage.FIELD_ABOUT_COMPANY, symbol * int(quantity))
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_ABOUT_COMPANY)
        if symbol == 's':
            assert main_page_obj.wait_no_error_field(FieldsMainPage.ERR_ABOUT_COMPANY_QUANTITY)
        else:
            assert main_page_obj.wait_main_page(FieldsMainPage.ERR_ABOUT_COMPANY_FORMAT)

    @allure.title('Поле your proj не проходит валидацию при некорректном заполнении')
    @allure.description('Я выделил следующие негативные проверки на валидацию поля your proj:'
                        'Количество символов = 1001, 1005')
    @pytest.mark.parametrize('quantity', ['1001', '1005'])
    def test_incorrect_field_your_proj(self, web_driver, quantity):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.scroll_page(FormsMainPage.FORM_ABOUT_COMPANY)
        main_page_obj._send_keys(FieldsMainPage.FIELD_ABOUT_COMPANY, 's' * int(quantity))
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_ABOUT_COMPANY)
        assert main_page_obj.wait_main_page(FieldsMainPage.ERR_ABOUT_COMPANY_QUANTITY)
