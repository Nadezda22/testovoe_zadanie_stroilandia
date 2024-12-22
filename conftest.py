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

#фикстура логгера для тестов
@pytest.fixture
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    yield logger
