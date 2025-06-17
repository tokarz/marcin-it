import pytest
import json
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

with open("config.json") as f:
    config = json.load(f)


def test_check_category_sport_teams():
  with sync_playwright() as p:
       
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])

        text_to_find = ".teams h1"
        try:
            element = page.wait_for_selector(text_to_find, timeout=5000)
        except PlaywrightTimeoutError:
            pytest.fail(f"Nie znaleziono selektora: TEAMS w ciągu 5 sekund")
        selector_text = element.text_content()
        assert selector_text == "Sport Teams", f"Oczekiwano: 'Sport Teams', ale znaleziono: '{selector_text}'"

        browser.close()
def test_check_category_players():
    with sync_playwright() as p:
       
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])

        text_to_find = ".players h1"
        try:
            element = page.wait_for_selector(text_to_find, timeout=5000)
        except PlaywrightTimeoutError:
            pytest.fail(f"Nie znaleziono selektora: PLAYERS w ciągu 5 sekund")
        selector_text = element.text_content()
        assert selector_text == "Players", f"Oczekiwano: 'Players', ale znaleziono: '{selector_text}'"

def test_check_category_coach():
    with sync_playwright() as p:
       
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(config["base_url"])
     
        text_to_find = ".coach h1"
        try:
            element = page.wait_for_selector(text_to_find, timeout=5000)
        except PlaywrightTimeoutError:
            pytest.fail(f"Nie znaleziono selektora: {text_to_find} w ciągu 5 sekund")
        selector_text = element.text_content()
        assert selector_text == "Coach", f"Oczekiwano: 'Coach', ale znaleziono: '{selector_text}'"



        