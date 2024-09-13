

class AddToCart():
    def __init__(self,page):
        self.page = page
        self._addToCart_labs_bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")
        self._remove_from_cart_labs_bike_light = page.locator("//button[@id='remove-sauce-labs-bike-light']")

    def add_bike_light(self):
        self._addToCart_labs_bike_light.click()

    def remove_bike_light(self):
        self._remove_from_cart_labs_bike_light.click()