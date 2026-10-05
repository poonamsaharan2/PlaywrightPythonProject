import pytest
from playwright.sync_api import expect

from page.login_page import LoginPage
from data.test_data import NEGATIVE_LOGIN_DATA
@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password",
    NEGATIVE_LOGIN_DATA
)
def test_invalid_login(page, username, password):
    login_page = LoginPage(page)

    login_page.login(username=username, password=password)

    expect(login_page.login_error).to_be_visible()

