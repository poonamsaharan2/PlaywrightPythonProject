class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.backpack = page.get_by_text("Sauce Labs Backpack")
        self.add_to_cart_backpack = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart = page.locator('[data-test="shopping-cart-link"]')

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def go_to_cart(self):
        self.cart.click()
