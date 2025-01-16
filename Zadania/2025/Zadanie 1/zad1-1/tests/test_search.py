from pom.search import SearchPage
from playwright.sync_api import sync_playwright




def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        search = SearchPage(page)

        search.navigate()
        search.search("playwright")

        browser.close()

test_search()
