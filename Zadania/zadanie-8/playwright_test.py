import pytest
from playwright.sync_api import sync_playwright

# CSS selectors for the input and button
input_selector = '.input-strobe'
enter_button_selector = '.enter-button'
success_class = '.level-header.completed'

# ANNOTACJA
@pytest.fixture(scope="module")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://flukeout.github.io/')
        yield page
        browser.close()

def run_css_t