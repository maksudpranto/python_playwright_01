
from pages.productListPage import ProductListPage

class LoginPage:
    def __init__(self,page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_text("Login")

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





