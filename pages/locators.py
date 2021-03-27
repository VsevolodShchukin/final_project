from selenium.webdriver.common.by import By

class MainLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_PRODUCT_IN_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    PRICE_OF_PRODUCT_IN_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")