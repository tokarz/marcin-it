from uczen import Uczen

class Klasa:
    def __init__(self , literaKlasy , numerKlasy ):
        self.literaKlasy = literaKlasy
        self.numerKlasy = numerKlasy
        self.uczniowie = [Uczen]
    def dodajUcznia(self , uczen):
        self.uczniowie.append(uczen)