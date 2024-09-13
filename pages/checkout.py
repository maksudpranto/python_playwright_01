class CheckoutPage():
    def __init__(self, page):
        self._item_1 = page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")
        self._item_2 = page.locator("//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self._cart_icon = page.locator("//a[@class='shopping_cart_link']")
        self._checkoutButton = page.locator("//button[@id='checkout']")
        self._firstName = page.locator("//input[@id='first-name']")
        self._lastName = page.locator("//input[@id='last-name']")
        self._zipCode = page.locator("//input[@id='postal-code']")
        self._continueButton = page.locator("//input[@id='continue']")
        self._emptyErrorMessage = page.locator("//div[@class='error-message-container error']")

    def addItem(self):
        self._item_1.click()
        self._item_2.click()

    def clickCartIcon(self):
        self._cart_icon.click()

    def clickCheckoutButton(self):
        self._checkoutButton.click()

    def formFillup(self):
        self._firstName.fill("Maksud Hossain")
        self._lastName.fill("Pranto")
        self._zipCode.fill("1206")
        self._continueButton.click()

    def emptyFormCheckout(self):
        self._continueButton.click()

    @property
    def emptyErrorMessage(self):
        return self._emptyErrorMessage

