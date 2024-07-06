import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from data import URL
from selenium.webdriver.chrome.options import Options


def get_driver(name):
    if name == 'Chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    else:
        raise TypeError('Driver is not found')


# эта фикстура возвращает генератор yield, он запускается каждый раз перед каждым тестом,
# также после каждого теста делается скриншот
@pytest.fixture
def web_driver():

    driver = get_driver('Chrome')
    driver.get(URL)

    yield driver
    allure.attach(driver.get_screenshot_as_png(),
                  name='!! Screenshot Captured !!',
                  attachment_type=allure.attachment_type.PNG)
    driver.quit()
