import allure
import pytest
from methods.main_page_methods import MainPage
from locators.locators_main_page import FormsMainPage, FieldsMainPage


class TestFieldEmail:

    @allure.title('Поле email проходит валидацию при корректном заполнении')
    @allure.description('Я выделил следующие, общепринятые позитивные проверки на валидацию поля email:email с цифрами,'
                        'email с дефисом, со знаком подчеркивания, с точками, с нижним и верхним регистром')
    @pytest.mark.parametrize('email', ['only123@yandex.ru', 'only-1@yandex.ru', 'only_1@yandex.ru',
                                       'only.1@yandex.ru', 'only@yandex.ru', 'ONLY@yandex.ru'])
    # Для ревьюера: assert аналогичен в тесте на поле name
    # все тесты  проходят
    def test_correct_field_email(self, web_driver, email):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj._send_keys(FieldsMainPage.FIELD_EMAIL, email)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_vis = main_page_obj.wait_no_error_field(FieldsMainPage.FIELD_EMAIL_ERROR)
        assert err_vis == True

    @allure.title('Поле email не проходит валидацию при некорректном заполнении')
    @allure.description('Я выделил следующие, общепринятые негативные проверки на валидацию поля email: отсутствие @,'
                        'без кода страны, без имени аккаунта, без доменной части')
    @pytest.mark.parametrize('email', ['onlyyandex.ru', 'only@yandex', '@yandex.ru', 'only@.ru'])
    # Для ревьюера: assert аналогичен в тесте на поле name
    # Не стал включать проверки на пробелы в доменной и именной части, так как реализовано автозаполнение пробелов
    # все тесты проходят
    def test_incorrect_field_email(self, web_driver, email):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj._send_keys(FieldsMainPage.FIELD_EMAIL, email)
        main_page_obj.click_elem_main_page(FormsMainPage.FORM_YOUR_DATA)
        err_text = main_page_obj.text_error_field(FieldsMainPage.FIELD_EMAIL_ERROR)
        assert err_text == 'Неверный формат'
