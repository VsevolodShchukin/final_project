from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainLocators

class ProductPage(BasePage):
    def add_to_cart_is_present(self):
        assert self.is_element_present(*MainLocators.ADD_TO_CART), "Error: cart-button is not present "
        print("Cart-button is present")

    def add_to_cart(self):
        btn_cart = self.browser.find_element(*MainLocators.ADD_TO_CART)
        btn_cart.click()
        print("Button was clicked. Product should be in basket")

    def checkout_of_product_name_in_cart(self):
        assert self.is_element_present(*MainLocators.NAME_OF_PRODUCT_IN_BASKET), "Error: there are no any product name in cart"
        product_name_in_basket = self.browser.find_element(*MainLocators.NAME_OF_PRODUCT_IN_BASKET).text
        product_name_in_title = self.browser.find_element(*MainLocators.NAME_OF_PRODUCT_IN_TITLE).text
        assert product_name_in_title == product_name_in_basket, "Error: titles are not equal"
        print("Titles are equal")

    def checkout_price_of_product(self):
        assert self.is_element_present(*MainLocators.PRICE_OF_PRODUCT_IN_BASKET), "Error: there are no any price in basket"
        price_in_title = self.browser.find_element(*MainLocators.PRICE_OF_PRODUCT_IN_TITLE).text
        print(f"Product price:{price_in_title}")
        price_in_basket = self.browser.find_element(*MainLocators.PRICE_OF_PRODUCT_IN_BASKET).text
        assert price_in_title == price_in_basket, f"Error: prices are not equal. Expected: {price_in_title}, actual: {price_in_basket}"
        print("Prices are equal")








