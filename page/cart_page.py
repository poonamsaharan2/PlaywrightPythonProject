class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_product = page.get_by_text("Sauce Labs Backpack")
        self.cart = page.locator('[data-test="shopping-cart-link"]')
        self.checkout_button = page.locator('[data-test="checkout"]')

    def go_to_cart(self):
        self.cart.click()

    def checkout(self):
        self.checkout_button.click()

