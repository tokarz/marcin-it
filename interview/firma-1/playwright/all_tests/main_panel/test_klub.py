
from pom.MainPanel.Klub import Klub

# G W T
def test_aktualnosci(klub: Klub):
    koncowyUrl = klub.click_club()
    assert koncowyUrl =="https://czarnijaslo.pl/category/wydarzenia/"
    