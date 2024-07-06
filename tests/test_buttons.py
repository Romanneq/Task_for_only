import allure
import pytest
from methods.main_page_methods import MainPage
from locators.locators_main_page import (FormsMainPage, CheckBoxAboutCompany, RadioButtonBudget, RadioButtonFeedback,
                                         Buttons)
from locators.locator_official_website import FormOfiicialWebsite


class TestButtons:

    @allure.title('Можно успешно кликнуть на кнопки в форме "О проекте"')
    @pytest.mark.parametrize('locators', [CheckBoxAboutCompany.CHECK_BOX_COMPLEX_WORKS,
                                          CheckBoxAboutCompany.CHECK_BOX_WEBSITE,
                                          CheckBoxAboutCompany.CHECK_BOX_SERVICE,
                                          CheckBoxAboutCompany.CHECK_BOX_DESIGN,
                                          CheckBoxAboutCompany.CHECK_BOX_UX,
                                          CheckBoxAboutCompany.CHECK_BOX_BRENDING])
    # Для ревьюера: в ассерте я выбрал локатор FORM_INTERACT_ID, так как при клике на кнопку в этот локатор
    # добавляется новый аттрибут
    # тесты проходят
    def test_click_buttons_form_about_proj(self, web_driver, locators):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.scroll_page(FormsMainPage.FORM_ABOUT_COMPANY)
        main_page_obj.click_elem_main_page(locators)
        assert main_page_obj.wait_main_page(FormsMainPage.FORM_INTERACT_ID)

    @allure.title('Можно кликнуть на кнопки в форме "Бюджет"')
    @pytest.mark.parametrize('locators', [RadioButtonBudget.BUTTON_MIN_2_MILLION,
                                          RadioButtonBudget.BUTTON_2_3_MILLION,
                                          RadioButtonBudget.BUTTON_3_5_MILLION,
                                          RadioButtonBudget.BUTTON_5_10_MILLION,
                                          RadioButtonBudget.BUTTON_10_20_MILLION,
                                          RadioButtonBudget.BUTTON_MORE_20_MILLION])
    # Для ревьюера: в ассерте я выбрал локатор FORM_INTERACT_ID, так как при клике на кнопку в этот локатор
    # добавляется новый аттрибут
    # тесты проходят
    def test_click_buttons_form_budget(self, web_driver, locators):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.scroll_page(FormsMainPage.FORM_BUDGET)
        main_page_obj.click_elem_main_page(locators)
        assert main_page_obj.wait_main_page(FormsMainPage.FORM_INTERACT_ID)

    @allure.title('Можно кликнуть на кнопки в форме "Откуда вы узнали о нас?"')
    @pytest.mark.parametrize('locators', [RadioButtonFeedback.BUTTON_RATING,
                                          RadioButtonFeedback.BUTTON_COPYRIGHT,
                                          RadioButtonFeedback.BUTTON_SOCIAL_NETWORK,
                                          RadioButtonFeedback.BUTTON_RECOM,
                                          RadioButtonFeedback.BUTTON_LONG_KNOW])
    # Для ревьюера: в ассерте я выбрал локатор FORM_INTERACT_ID, так как при клике на кнопку в этот локатор
    # добавляется новый аттрибут
    # тесты проходят
    def test_click_buttons_form_feedback(self, web_driver, locators):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.scroll_page(FormsMainPage.FORM_FEEDBACK)
        main_page_obj.click_elem_main_page(locators)
        assert main_page_obj.wait_main_page(FormsMainPage.FORM_INTERACT_ID)

    @allure.title('Клик на крестик ведет на официальную страницу сайта')
    # тест проходят
    def test_click_buttons_cross(self, web_driver):
        main_page_obj = MainPage(web_driver)
        main_page_obj.wait_main_page(FormsMainPage.FORM_YOUR_DATA)
        main_page_obj.click_elem_main_page(Buttons.BUTTON_CROSS)
        assert main_page_obj.wait_main_page(FormOfiicialWebsite.OFFICIAL_WEBSITE)
