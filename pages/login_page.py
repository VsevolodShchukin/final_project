from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "No such login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM)
        email_form.send_keys(email)
        password_form1 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FORM)
        password_form1.send_keys(password)
        password_form2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FORM2)
        password_form2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.BTN_SUBMIT_REG)
        btn.click()



