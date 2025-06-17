import pytest
from playwright.sync_api import sync_playwright
import json


with open("config.json") as f:
    config = json.load(f)


def test_check_category_coach():
  with sync_playwright() as p:
       
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(config["base_url"])

        selector_team = page.locator(".teams li:first-child")
        selector_team.click()

        coach_selector = ".coach span"
        page.wait_for_selector(coach_selector)
        coach_selector_count = page.locator(".coach span").count()
    
        assert coach_selector_count > 0   , print("lista jest pusta!")



