from turtledemo.clock import setup
from pages.checkout import CheckoutPage
from playwright.sync_api import Page,expect
from pages.checkout import CheckoutPage
from pages.loginPage import LoginPage
from test_cases.conftest import set_up_tear_down


def test_checkout(set_up_tear_down)->None:
    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")

    # Adding item to Cart
    add_items = CheckoutPage(page)
    add_items.addItem()

    # Clicking the Cart Icon
    click_cart = CheckoutPage(page)
    click_cart.clickCartIcon()

    # Redirect to Information Page
    clickCheckout = CheckoutPage(page)
    clickCheckout.clickCheckoutButton()

    # Filling the form
    form_fillup = CheckoutPage(page)
    form_fillup.formFillup()


def test_without_formFillup(set_up_tear_down)->None:

    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_page = LoginPage(page)
    login_done = login_page.perform_login(credentials)
    expect(login_done.product_header).to_have_text("Products")

    # Adding item to Cart
    add_items = CheckoutPage(page)
    add_items.addItem()

    # Clicking the Cart Icon
    click_cart = CheckoutPage(page)
    click_cart.clickCartIcon()

    # Redirect to Information Page
    clickCheckout = CheckoutPage(page)
    clickCheckout.clickCheckoutButton()
    click_continue = CheckoutPage(page)
    click_continue.emptyFormCheckout()

    error_message = "Error: First Name is required"
    expect(click_continue.emptyErrorMessage).to_have_text(error_message)






