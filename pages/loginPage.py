
from pages.productListPage import ProductListPage

class LoginPage:
    def __init__(self,page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_text("Login")
        self._error_message_for_invalid = page.locator("//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
        self._error_message_for_empty = page.locator("//h3[normalize-space()='Epic sadface: Username is required']")
        self._error_message_without_login = page.locator("//h3[@data-test='error']")


    def enter_username(self,u_name):
        self._username.clear()
        self._username.fill(u_name)

    def enter_password(self,p_word):
        self._password.clear()
        self._password.fill(p_word)

    def click_login_button(self):
        self._login_button.click()

    def perform_login(self,credentials):
        self.enter_username(credentials['username'])
        self.enter_password(credentials['password'])

        self.click_login_button()
        return ProductListPage(self.page)


    @property
    def error_message_for_invalid(self):
        return self._error_message_for_invalid

    @property
    def error_message_for_empty(self):
        return self._error_message_for_empty

    @property
    def error_message_without_login(self):
        return self._error_message_without_login

    @property
    def login_button(self):
        return self._login_button

