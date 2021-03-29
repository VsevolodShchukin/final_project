from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart_is_present(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Error: cart-button is not present "
        print("Cart-button is present")

    def add_to_cart(self):
        btn_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        btn_cart.click()
        print("Button was clicked")

    def message_of_adding_product_is_present(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_OF_ADDING), "There are no any success-message of product adding"
        print("Product was added")

    def are_titles_equal(self):
        assert self.is_element_present(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET), "There are no any product name in basket"
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET).text
        product_name_in_title = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_TITLE).text
        assert product_name_in_title == product_name_in_basket, "Titles are not equal"
        print("Titles are equal")

    def are_prices_equal(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_OF_PRODUCT_IN_BASKET), "There are no any price in basket"
        price_in_title = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_TITLE).text
        print(f"Product price:{price_in_title}")
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_BASKET).text
        assert price_in_title == price_in_basket, f"Prices are not equal. Expected: {price_in_title}, actual: {price_in_basket}"
        print("Prices are equal")

    def message_of_adding_product_is_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_OF_ADDING), "There is success-message of product adding"
        print("There are no any success-message of product adding")

    def message_of_adding_product_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_OF_ADDING), "Success-message of product adding is not disappeared"
        print("Success-message of product adding is disappeared")


class ProductPageScripts(ProductPage):

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.open_browser()
        self.add_to_cart_is_present()
        self.add_to_cart()
        self.message_of_adding_product_is_not_present()

    def test_guest_cant_see_success_message(self):
        self.open_browser()
        self.add_to_cart_is_present()
        self.message_of_adding_product_is_not_present()

    def test_message_disappeared_after_adding_product_to_basket(self):
        self.open_browser()
        self.add_to_cart_is_present()
        self.add_to_cart()
        self.message_of_adding_product_is_disappeared()









