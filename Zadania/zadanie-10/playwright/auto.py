from hamulec import Hamulec
from kierownica import Kierownica
from kolo import Kolo
from silnik import Silnik

class Auto:
    def __init__(self):
        self.silnik = Silnik()
        self.kola = [Kolo(), Kolo()]
        self.hamulce = [Hamulec(), Hamulec()]
        self.kierownica = Kierownica()

    def opis(self):
        print(self.kierownica.hello())
        print(self.silnik.hello())
        for kolo in self.kola:
            print(kolo.hello())
        for hamulec in self.hamulce:
            print(hamulec.hello())


uruchom_auto = Auto()

uruchom_auto.opis()