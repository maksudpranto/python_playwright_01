from playwright.sync_api import Page,expect

def test_valid_login(page: Page)->None:
    page.goto("https://saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()

    product_header = page.locator("//span[@class='title']")
    expect(product_header).to_have_text("Products")


def test_invalid_login(page: Page)->None:
    page.goto("https://saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauces")
    page.get_by_text("Login").click()


    expected_error_message = page.locator("//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
    expect(expected_error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")

def test_login_without_credentials(page: Page)->None:
    page.goto("https://saucedemo.com")
    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("")
    page.get_by_text("Login").click()

    expected_error_message = page.locator("//div[@class='error-message-container error']")
    expect(expected_error_message).to_contain_text("Epic sadface: Username is required")
