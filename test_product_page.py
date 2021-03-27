import time
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open_browser()
    page.add_to_cart_is_present()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.checkout_of_product_name_in_cart()
    page.checkout_price_of_product()


