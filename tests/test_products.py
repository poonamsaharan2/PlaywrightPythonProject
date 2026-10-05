import pytest
from page.products_page import ProductsPage
from playwright.sync_api import expect
from page.login_page import LoginPage
from page.cart_page import CartPage
from data.test_data import LOGIN_DATA, CUSTOMER_DATA
from page.checkout_page import CheckoutPage
@pytest.mark.smoke
@pytest.mark.regression
def test_products(page):
    login_page = LoginPage(page)
    login_page.login(LOGIN_DATA["USERNAME"], LOGIN_DATA["PASSWORD"])
    products_page = ProductsPage(page)
    expect(products_page.backpack).to_be_visible()
    products_page.add_backpack_to_cart()
    expect(products_page.cart_badge).to_have_text("1")
    products_page.go_to_cart()
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    expect(cart_page.cart_product).to_be_visible()
    cart_page.checkout()
    checkout_page.enter_customer_information(
        first_name=CUSTOMER_DATA["FIRST_NAME"],
        last_name=CUSTOMER_DATA["LAST_NAME"],
        zip_code=CUSTOMER_DATA["ZIP_CODE"]
    )
    checkout_page.click_continue()
    checkout_page.click_finish()
    expect(checkout_page.order_confirmation).to_have_text("Thank you for your order!")

