class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.zip_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.order_confirmation = page.locator('[data-test="complete-header"]')

    def enter_customer_information(self,first_name,last_name,zip_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()
