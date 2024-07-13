import allure
import pytest
from methods.main_page_methods import MainPage
from locators.locators_main_page import FormsMainPage, FieldsMainPage


class TestFieldCompany:

    @allure.title('Поле company проходит валидацию при корректном заполнении')
    @allure.description('Я выделил следующие, общепринятые позитивные проверки на валидацию поля company:'
                        'ОАО в кавычках, без кавычек, русские буквы, латинские буквы, спецсимволы, точка, запятая')
    @pytest.mark.parametrize('company', ['"ОАО" Only', 'ОАО Only', 'ОАО Онли', 'Only/QA', 'Only.QA'])
    # Для ревьюера: assert аналогичен в тесте на поле name
    # 1 тест падает, 4 проходят
    def test_correct_field_company(self, web_driver, company):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj._send_keys(FieldsMainPage.FIELD_COMPANY, company)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_vis = main_page_obj.wait_no_error_field(FieldsMainPage.FIELD_COMPANY_ERROR)
        assert err_vis == True

    @allure.title('Поле company не проходит валидацию при некорректном заполнении')
    @allure.description('Я выделил следующие, общепринятые негативные проверки на валидацию поля company: '
                        'только спецсимволы, только цифры, пробел, пустое поле')
    @pytest.mark.parametrize('company', ['@##', '123', ' ', ''])
    # Для ревьюера: assert аналогичен в тесте на поле name
    # 1 тест падает, 3 проходят
    def test_incorrect_field_company(self, web_driver, company):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj._send_keys(FieldsMainPage.FIELD_COMPANY, company)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_text = main_page_obj.text_error_field(FieldsMainPage.FIELD_COMPANY_ERROR)
        assert err_text == 'Неверный формат' or 'Обязательное поле'
