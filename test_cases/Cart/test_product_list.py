from playwright.sync_api import Page,expect
from pages.loginPage import LoginPage
from pages.productListPage import ProductListPage

def test_add_to_cart(set_up_tear_down):
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)

    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")

    product_name = "Sauce Labs Bike Light"
    product_page = ProductListPage(page)

    product_page.add_bike_light()

def test_remove_from_cart(set_up_tear_down):
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)

    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")

    product_name = "Sauce Labs Bike Light"
    product_page = ProductListPage(page)

    product_page.add_bike_light()
    product_page.remove_bike_light()
