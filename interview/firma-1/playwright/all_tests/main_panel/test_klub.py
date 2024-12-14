
from pom.MainPanel.Klub import Klub




def test_aktualnosci(klub):
    koncowyUrl = klub.click_club()
    assert koncowyUrl =="https://czarnijaslo.pl/category/wydarzenia/"
    