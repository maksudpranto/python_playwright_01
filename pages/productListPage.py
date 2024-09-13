class ProductListPage:
    def __init__(self,page):
        self.page = page
        self._products_header = page.locator("//span[@class='title']")
        self._hamburger_menu = page.locator("//button[@id='react-burger-menu-btn']")
        self._logout_button = page.locator("//a[@id='logout_sidebar_link']")
        # Select a Product and add to cart




    def click_hamburger_menu(self):
        self._hamburger_menu.click()

    def click_logout_button(self):
        self._logout_button.click()


    def perform_logout(self):
        self.click_hamburger_menu()
        self.click_logout_button()


    @property
    def product_header(self):
        return self._products_header


        