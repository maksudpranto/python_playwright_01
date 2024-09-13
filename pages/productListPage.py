from playwright.sync_api import expect


class ProductListPage:
    def __init__(self,page):
        self.page = page
        self._products_header = page.locator("//span[@class='title']")

    @property
    def product_header(self):
        return self._products_header
