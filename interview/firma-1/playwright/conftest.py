import pytest
from all_tests.main_panel.test_aktualnosci import Aktualnosci
from all_tests.main_panel.test_klub import Klub
from playwright.sync_api import Page
from all_tests.Stopka.test_stopki import Stopka
from all_tests.Sponsoring.test_sponsoring import Sponsoring
from all_tests.Tabela.test_tabeli import Tabela
from all_tests.SocialMedia.test_socialMedia import SocialMedia
from all_tests.Artykuly.test_artykulow import Artykuly
from all_tests.Wyszukiwarka.test_wyszukiwarki import Wyszukiwarka

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
def sponsoring(page: Page) -> Sponsoring:
    return Sponsoring(page)


@pytest.fixture
def socialmedia(page :  Page) -> SocialMedia:
    return SocialMedia(page)

@pytest.fixture
def tabela(page : Page) -> Tabela:
    return Tabela(page)

@pytest.fixture
def artykuly(page : Page) -> Artykuly:
    return Artykuly(page)

@pytest.fixture
def wyszukiwanie(page: Page) -> Wyszukiwarka:
    return Wyszukiwarka(page)