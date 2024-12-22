


def test_go_to_store_page(browser, logger):
    store_name = browser.find_element("xpath", '//div[@class="container-fluid header-v2 logo-row"]//a[@class="header-v2-logo"]')
    catalog = browser.find_element("xpath", '//div[@class="header-v2-catalog-button"]')
    search_bar = browser.find_element("xpath", '//div[@class="search-input-div"]//input[@class="search-input"]')

    message = "Логотип магазина, кнопка каталога, строка поиска были найдены на странице"
    logger.info(message)


def test_add_product_to_the_cart(browser, logger):
    city = browser.find_element("xpath", '//div[@class="cities-locate__buttons"]//a[text()="Да"]')
    city.click()

    accept_cookies = browser.find_element("xpath", '//div[@class="cookie-block"]//button[@data-role="cooke-accept-btn"]')
    accept_cookies.click()

    button_catalog = browser.find_element("xpath", '//div[@class="small-banners-block"]//div[@data-creative="Новогодние куклы и фигурки |№1"]')
    button_catalog.click()
    product = browser.find_element("xpath", '//div[@data-name="Фигурка новогодняя Снеговик в ушанке 47-71 см"]//div[@data-role="basket-add"]')
    product.click()

    message = "товар успешно добавлен в корзину"

    logger.info(message)


def test_go_to_basket(browser, logger):
    city = browser.find_element("xpath", '//div[@class="cities-locate__buttons"]//a[text()="Да"]')
    city.click()
    accept_cookies = browser.find_element("xpath", '//div[@class="cookie-block"]//button[@data-role="cooke-accept-btn"]')
    accept_cookies.click()

    basket = browser.find_element("xpath", '//div[@class="container-fluid header-v2 logo-row"]//span[text()="Корзина"]')
    basket.click()

    product = browser.find_element("xpath", '//div[@class="basket-item__content"]//a[text()="Фигурка новогодняя Снеговик в ушанке 47-71 см"]')
    #todo выбрать другой продукт
    product_price = browser.find_element("xpath", '//div[@class="basket-price__current-price"]//span[text()="1 090 ₽"]')
    price = int(product_price.get_attribute())

    button_add = browser.find_element("xpath", '//div[@class="counter"]//a[@class="counter__plus"]')

    for i in range(2):
        button_add.click()
        message = 'добавил 2 единицы тoвaра'
        logger.info(message)

    total_price = browser.find_element("xpath", '//div[@class="total-row total-row--total">3 270 ₽]')
    value_for_total_price = int(total_price.get_attribute())

    assert price < value_for_total_price







