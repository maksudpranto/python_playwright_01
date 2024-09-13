from playwright.sync_api import Page,expect
from pages.productListPage import ProductListPage
from pages.loginPage import LoginPage


def test_logout(set_up_tear_down)->None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    login_page.perform_login(credentials)

    productListpage = ProductListPage(page)
    productListpage.perform_logout()

    # Log Out


    expect(login_page.login_button).to_be_visible()