import pytest
import time


@pytest.mark.tryfirst
def test_go_to_store_page(browser, add_cookie_and_city, logger):
    store_name = browser.find_element("xpath",
                                      '//div[@class="container-fluid header-v2 logo-row"]//a[@class="header-v2-logo"]')
    catalog = browser.find_element("xpath", '//div[@class="header-v2-catalog-button"]')
    search_bar = browser.find_element("xpath", '//div[@class="search-input-div"]//input[@class="search-input"]')

    message = "Логотип магазина, кнопка каталога, строка поиска были найдены на странице"
    logger.info(message)


@pytest.mark.xfail
def test_add_product_to_the_cart(browser, add_cookie_and_city, logger):
    time.sleep(10)
    button_catalog = browser.find_element("xpath",
                                          '//a[@href="/catalog/elektroinstrument/?SORT=discount_size"]//child::*')
    button_catalog.click()

    value_in_catalog = browser.find_element("xpath", '//a[@href="/catalog/dreli-shurupoverty/"]//child::*')
    value_in_catalog.click()

    add_produckt = browser.find_element("xpath", '//div[@data-item="15576845"]//div[@data-role="basket-add"]')
    add_produckt.click()

    message = "товар успешно добавлен в корзину"
    logger.info(message)


@pytest.mark.trylast
def test_go_to_basket(browser, add_cookie_and_city, add_to_basket, logger):
    basket = browser.find_element("xpath", '*//a[@href="/cart/"]')
    basket.click()

    product_price = browser.find_element("xpath", '//div[@class="basket-price__current-price"]//span')
    price = int(product_price.text.replace(' ₽', '').replace(' ', ''))

    button_add = browser.find_element("xpath", '//div[@class="counter"]//a[@class="counter__plus"]')

    for i in range(2):
        button_add.click()
        message = 'добавил 2 единицы товара'
        logger.info(message)

    total_price = browser.find_element("xpath",'//div[@class="total-row total-row--total"]//div[@class="total-row__value"]')
    value_for_total_price = int(total_price.text.replace(' ₽', '').replace(' ', ''))

    assert price * 3 == value_for_total_price
