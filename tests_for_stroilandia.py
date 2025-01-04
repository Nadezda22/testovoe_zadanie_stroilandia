import time


def test_go_to_store_page(browser, add_city_and_cookies, logger):
    store_name = browser.find_element("xpath", '//div[@class="container-fluid header-v2 logo-row"]//a[@class="header-v2-logo"]')
    catalog = browser.find_element("xpath", '//div[@class="header-v2-catalog-button"]')
    search_bar = browser.find_element("xpath", '//div[@class="search-input-div"]//input[@class="search-input"]')

    message = "The store's logo, catalog button, and search bar were found on the page"
    logger.info(message)


def test_add_product_to_the_cart(browser, add_city_and_cookies, logger):
    time.sleep(3)
    button_catalog = browser.find_element("xpath", '//div[@class="wrap"]//child::*//div')
    button_catalog.click()
    logger.info('clicked the catalog button')

    value_in_catalog = browser.find_element("xpath", '//div[@class="simplebar-content-wrapper"]//a[@href="/catalog/mebel/"]')
    value_in_catalog.click()
    logger.info('selected a group from the catalog')

    list_products = browser.find_element("xpath", '//div[@class="subsection_item"]//a[@href="/catalog/stoli/"]')
    list_products.click()
    logger.info('selected a list of products')

    product_category = browser.find_element("xpath", '//div[@class="subsection_item"]//a[@href="/catalog/stoly-obedennye/"]')
    product_category.click()
    logger.info('selected a product category')

    buy_product = browser.find_element("xpath", '//div[@data-name="Стол обеденный SV-МЕБЕЛЬ СО-1 900х740х600 мм белый"]')
    buy_product.click()
    logger.info('selected a product')

    basket_add = browser.find_element("xpath", '//div[@class="p_product_shoping--wrapper"]//button[@data-role="basket-add"]')
    basket_add.click()
    logger.info('product was successfully added to the cart')


def test_go_to_basket(browser, add_city_and_cookies, add_to_basket, logger):
    basket = browser.find_element("xpath", '//div[@class="logo_and_menu-row"]//div[@class="container-fluid header-v2 logo-row"]//a[@data-link="/cart/"]')
    basket.click()

    product_price = browser.find_element("xpath", '//div[@class="basket-item__price basket-price"]//div[@class="basket-price__current"]')
    price = float(product_price.text.replace(' ₽', '').replace(' ', ''))

    button_add = browser.find_element("xpath", '//div[@class="basket-item"]//div[@class="counter"]//a[@data-role="basket-plus"]')
    browser.refresh()

    for i in range(2):
        button_add.click()
    message = 'added 2 items'
    logger.info(message)

    total_price = browser.find_element("xpath", '//div[@class="total__block total-sum"]//div[@class="total-row total-row--total"]//div[@class="total-row__value"]')
    value_for_total_price = float(total_price.text.replace(' ₽', '').replace(' ', ''))

    assert price * 3 == value_for_total_price
