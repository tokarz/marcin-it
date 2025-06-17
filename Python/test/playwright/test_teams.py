import pytest
from playwright.sync_api import sync_playwright
import json


with open("config.json") as f:
    config = json.load(f)


def test_check_category_sport_teams():
  with sync_playwright() as p:
       
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(config["base_url"])

        players_selector = page.locator(".players")
        players_selector.wait_for()
        
        players_count_selector = page.locator(".player ul li")
        players_count = players_count_selector.count()

        assert players_count == 0 , print("lista nie jest pusta!")

        selector_team = page.locator(".teams li:first-child")
        selector_team.click()

        page.wait_for_selector(".players ul li")
        players_cout_selector2 = page.locator(".players ul li")
        players_count2 = players_cout_selector2.count()

        assert players_count2 > 0 , print("lista jest pusta!")


        
