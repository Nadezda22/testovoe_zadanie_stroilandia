import pytest
import logging
from selenium import webdriver

# ссылка приложения
test_url = "https://stroylandiya.ru/"


# фикстура браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    url = test_url
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


# фикстура логгера для тестов
@pytest.fixture
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    yield logger


# фикстура для добавления города и файлов cookies
@pytest.fixture
def add_cookie_and_city(browser):
    city = browser.find_element("xpath", '//div[@class="cities-locate__buttons"]//a[text()="Да"]')
    city.click()
    accept_cookies = browser.find_element("xpath", '//div[@class="cookie-block"]//button[@data-role="cooke-accept-btn"]')
    accept_cookies.click()


@pytest.fixture()
def add_to_basket(browser, add_cookie_and_city):
    button_catalog = browser.find_element("xpath",'//a[@href="/catalog/elektroinstrument/?SORT=discount_size"]//child::*')
    button_catalog.click()

    value_in_catalog = browser.find_element("xpath", '//a[@href="/catalog/dreli-shurupoverty/"]//child::*')
    value_in_catalog.click()

    add_produckt = browser.find_element("xpath", '//div[@data-item="15555486"]//div[@data-role="basket-add"]')
    add_produckt.click()
