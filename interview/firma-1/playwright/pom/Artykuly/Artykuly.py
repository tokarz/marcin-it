from pom.Utilities.Utilities import Utilities

class Artykuly:
    def __init__(self, page):
        self.page = page
        self.utils = Utilities(page)

    def sprawdz_nazwe_artykul1(self):
        self.utils.sprawdz_poprawnosc_tytulu_artykulu(1)
        print("OK")

    def sprawdz_nazwe_artykul2(self):
        self.utils.sprawdz_poprawnosc_tytulu_artykulu(2)
        print("OK")

    def sprawdz_nazwe_artykul4(self):
        self.utils.sprawdz_poprawnosc_tytulu_artykulu(4)
        print("OK")

    def sprawdz_nazwe_artykul6(self):
        self.utils.sprawdz_poprawnosc_tytulu_artykulu(6)
        print("OK")
        