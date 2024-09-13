from playwright.sync_api import Page,expect



def test_logout(page: Page)->None:
    page.goto("https://saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()
    product_header = page.locator("//span[@class='title']")
    expect(product_header).to_have_text("Products")

    # Log Out

    click_burger_menu = page.locator("//button[@id='react-burger-menu-btn']").click()
    click_logout = page.locator("//a[@id='logout_sidebar_link']").click()

    login_button_verification = page.get_by_text("Login")
    expect(login_button_verification).to_be_visible()
