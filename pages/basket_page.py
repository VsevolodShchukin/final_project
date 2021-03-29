from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "No such login url"

    def items_in_basket_are_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "There are items in basket"
        print("There are no any items in basket")

    def is_basket_empty(self):
        basket_is_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert basket_is_empty_text, "Basket is not empty"
        print("Basket is empty")
