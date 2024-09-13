from playwright.sync_api import Page,expect
from pages.loginPage import LoginPage


def test_valid_login(set_up_tear_down)->None:
    page = set_up_tear_down
    credentials = {'username':'standard_user','password':'standard_user'}
    login_page = LoginPage(page)
    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")


def test_invalid_login(set_up_tear_down)->None:
    page = set_up_tear_down
    credentials = {'username':'standard_users','password':'password'}
    login_page = LoginPage(page)
    login_page.perform_login(credentials)

    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    expect(login_page.error_message_for_invalid).to_contain_text(expected_error_message)

def test_login_without_credentials(set_up_tear_down)->None:
    page = set_up_tear_down
    login_page = LoginPage(page)
    login_page.click_login_button()

    expected_message = "Epic sadface: Username is required"
    expect(login_page.error_message_for_empty).to_contain_text(expected_message)


def test_access_inventory_without_login(set_up_tear_down)->None:
    page = set_up_tear_down
    page.goto("https://www.saucedemo.com/inventory.html")
    login_page = LoginPage(page)
    expect(login_page.error_message_without_login).to_contain_text("Epic sadface: You can only access '/inventory.html' when you are logged in.")





