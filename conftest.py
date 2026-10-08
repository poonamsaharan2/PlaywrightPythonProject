import os
import pytest
from playwright.sync_api import sync_playwright
from data.test_data import BASE_URL

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")
            page.context.tracing.stop(path=f"traces/{item.name}.zip")
@pytest.fixture
def page():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false").lower() == "true"
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto(BASE_URL)
        yield page
        context.close()
        browser.close()
@pytest.fixture
def api_request(playwright):
    request = playwright.request.new_context()
    yield request
    request.dispose()