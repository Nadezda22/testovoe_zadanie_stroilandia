#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import logging
import time
import undetected_chromedriver as uc
from wheel.metadata import yield_lines

# ссылка приложения
test_url = "https://stroylandiya.ru/"


# фикстура браузера
@pytest.fixture
def browser():
    driver = uc.Chrome()
    url = test_url
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


# фикстура логгера для тестов
@pytest.fixture
def logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('logfile.txt')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    yield logger

# фикстура для выбора города доставки и cookies
@pytest.fixture
def add_city_and_cookies(browser, logger):
    city = browser.find_element("xpath", '//div[@class="cities-locate__buttons"]//a[text()="Да"]')
    city.click()
    message = 'the city for product delivery has been successfully selected'
    logger.info(message)

    time.sleep(3)

    accept_cookies = browser.find_element("xpath", '//div[@class="cookie-block"]//button[@data-role="cooke-accept-btn"]')
    accept_cookies.click()
    message = 'cookies have been successfully added by the user'
    logger.info(message)


@pytest.fixture()
def add_to_basket(browser, add_city_and_cookies, logger):
    button_catalog = browser.find_element("xpath", '//div[@class="small-banners-block"]//a[@href="/catalog/keramicheskii-granit/?SORT=discount_size"]')
    button_catalog.click()
    logger.info('clicked the catalog button')

    value_in_catalog = browser.find_element("xpath", '//div[@class="swiper-wrapper"]//div[@data-name="Керамический гранит GLOBALGRES Imperator 60х60 см белый"]')
    value_in_catalog.click()

    add_produckt = browser.find_element("xpath", '//div[@class="p_product_shoping--wrapper"]//button[@data-role="basket-add"]')
    add_produckt.click()
    logger.info('product was successfully added to the cart')
