from playwright.sync_api import sync_playwright,expect

from page import cart_page
from page.login_page import LoginPage
from page.products_page import ProductsPage

def test_swag_labs(page):
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")
        #for product
        products_page = ProductsPage(page)
        expect(products_page.backpack).to_be_visible()

