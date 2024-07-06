from selenium.webdriver.common.by import By


class FieldsMainPage:
    FIELD_NAME = [By.XPATH, ".//input[@name = 'name']"]  # локатор поля Имя
    FIELD_NAME_ERROR = [By.XPATH, ".//form/div[1]/div/div[1]/div/input[@error]"]  # локатор ошибки поля name
    FIELD_EMAIL = [By.XPATH, ".//input[@name = 'email']"]  # локатор поля email
    FIELD_EMAIL_ERROR = [By.XPATH, ".//div[2]/div/input[@error]"]  # локатор ошибки поля email
    FIELD_COMPANY = [By.XPATH, ".//input[@name = 'company']"]  # локатор поля Компания
    FIELD_COMPANY_ERROR = [By.XPATH, ".//div[4]/div/input[@error]"]  # локатор ошибки поля Компания
    FIELD_TEL = [By.XPATH, ".//input[@name = 'phone']"]  # локатор поля номер телефона
    FIELD_TEL_ERROR = [By.XPATH, ".//div[3]/div/div[1]/input[@error]"]  # локатор ошибки поля Телефон
    FLAG_TEL = [By.XPATH, ".//div[@class='iti__selected-flag']"]  # локатор флага выбора другой страны
    COUNTRY_BEL = [By.XPATH, ".//li[@data-country-code = 'by'][1]"]  # локатор страны Беларусь в списке стран
    BEL_TEL = [By.XPATH, ".//div[@title = 'Belarus (Беларусь)']"]  # локатор выбранной страны в поле телефон
    FIELD_ABOUT_COMPANY = [By.XPATH, ".//textarea[@name = 'description']"]  # локатор поля "Расскажите о вашем проекте"
    ERR_ABOUT_COMPANY_QUANTITY = [By.XPATH, ".//p[text()='Превышено максимальное количество символов']"]  # локатор ошибки количества символов поля "Расскажите о вашем проекте"
    ERR_ABOUT_COMPANY_FORMAT = [By.XPATH, ".//p[text()='Неверный формат']"]  # локатор ошибки формата данных в поле "Расскажите о вашем проекте"


class FormsMainPage:
    FORM_YOUR_DATA = [By.XPATH, ".//p[text()='Ваши контакты']"]  # локатор поля "Ваши контакты"
    FORM_ABOUT_COMPANY = [By.XPATH, ".//p[text() = 'О проекте']"]  # локатор формы "О проекте"
    FORM_BUDGET = [By.XPATH, ".//p[text() = 'Бюджет']"]  # локатор формы "Бюджет"
    FORM_FEEDBACK = [By.XPATH, ".//p[text()='Откуда вы узнали о нас?']"]  # локатор формы "Откуда вы узнали о нас?"
    FORM_INTERACT_ID = [By.XPATH, ".//form[@data-gtm-form-interact-id]"]  # локатор всех форм, при клике на кнопку добавляет новый аттрибут


class CheckBoxAboutCompany:
    CHECK_BOX_COMPLEX_WORKS = [By.XPATH, ".//input[@value = 'Комплекс работ']/.."]  # локатор чекбокса "Комплекс работ"
    CHECK_BOX_WEBSITE = [By.XPATH, ".//input[@value = 'Сайт']/.."]  # локатор чекбокса "Сайт"
    CHECK_BOX_SERVICE = [By.XPATH, ".//input[@value = 'Сервис']/.."]  # локатор чекбокса "Сервис"
    CHECK_BOX_DESIGN = [By.XPATH, ".//input[@value = 'Дизайн']/.."]  # локатор чекбокса "Дизайн"
    CHECK_BOX_UX = [By.XPATH, ".//input[@value = 'UX-аудит']/.."]  # локатор чекбокса "UX-аудит"
    CHECK_BOX_BRENDING = [By.XPATH, ".//input[@value = 'Брендинг']/.."]  # локатор чекбокса "Брендинг"


class RadioButtonBudget:
    BUTTON_MIN_2_MILLION = [By.XPATH, ".//input[@value='Менее 2 млн']/.."]  # локатор радиокнопки менее 2 миллионов
    BUTTON_2_3_MILLION = [By.XPATH, ".//input[@value='2-3 млн']/.."]  # локатор радиокнопки 2-3 миллиона
    BUTTON_3_5_MILLION = [By.XPATH, ".//input[@value='3–5 млн']/.."]  # локатор радиокнопки 3-5 миллиона
    BUTTON_5_10_MILLION = [By.XPATH, ".//input[@value='5–10 млн']/.."]  # локатор радиокнопки 5-10 миллиона
    BUTTON_10_20_MILLION = [By.XPATH, ".//input[@value='10-20 млн']/.."]  # локатор радиокнопки 10-20 миллионов
    BUTTON_MORE_20_MILLION = [By.XPATH, ".//input[@value='Более 20 млн']/.."]  # локатор радиокнопки более 20 миллионов


class RadioButtonFeedback:
    BUTTON_RATING = [By.XPATH, ".//input[@value='Рейтинги']/.."]  # локатор радиокнопки Рейтинги
    BUTTON_COPYRIGHT = [By.XPATH, ".//input[@value='Копирайт на сайте']/.."]  # локатор радиокнопки Копирайт на сайте
    BUTTON_SOCIAL_NETWORK = [By.XPATH, ".//input[@value='Соцсети']/.."]  # локатор радиокнопки Соцсети
    BUTTON_RECOM = [By.XPATH, ".//input[@value='Рекомендации']/.."]  # локатор радиокнопки Рекомендации
    BUTTON_LONG_KNOW = [By.XPATH, ".//input[@value='Давно знаю']/.."]  # локатор радиокнопки давно знаю


class Buttons:
    BUTTON_CROSS = [By.XPATH, "//*[@id='Header']/button"]  # локатор выхода из формы
