import pytest
from all_tests.main_panel.test_aktualnosci import Aktualnosci
from all_tests.main_panel.test_klub import Klub
from playwright.sync_api import Page

@pytest.fixture
def aktualnosci(page: Page) -> Aktualnosci:
    return Aktualnosci(page)

@pytest.fixture
def klub(page: Klub) -> Klub:
    return Klub(page)