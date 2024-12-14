import pytest
from all_tests.main_panel.test_aktualnosci import Aktualnosci
from all_tests.main_panel.test_klub import Klub
from playwright.sync_api import Page
from all_tests.Stopka.test_stopki import Stopka
from all_tests.Sponsoring.test_sponsoring import Sponsoring
from all_tests.Tabela.test_tabeli import Tabela

@pytest.fixture
def aktualnosci(page: Page) -> Aktualnosci:
    return Aktualnosci(page)

@pytest.fixture
def klub(page: Page) -> Klub:
    return Klub(page)

@pytest.fixture
def stopka(page: Page) -> Stopka:
    return Stopka(page)

@pytest.fixture
def sponsoring(page: Page):
    return Sponsoring(page)

@pytest.fixture
def tabela(page : Page):
    return Tabela(page)