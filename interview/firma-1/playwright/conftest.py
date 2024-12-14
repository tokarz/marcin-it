import pytest
from all_tests.main_panel.test_main_panel import Aktualnosci
from playwright.sync_api import Page

@pytest.fixture
def aktualnosci(page: Page) -> Aktualnosci:
    return Aktualnosci(page)