from playwright.sync_api import sync_playwright

from pom.search import SearchPage

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        search = SearchPage(page)

        search.navigate()
        search.search("playwright")

        # assert?

        browser.close()

test_search()
