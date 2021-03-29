from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_PRODUCT_IN_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    PRICE_OF_PRODUCT_IN_TITLE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    SUCCESS_MESSAGE_OF_ADDING = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_FORM2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_SUBMIT_REG = (By.NAME, "registration_submit")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
