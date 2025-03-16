from Wojownik import Wojownik

class Druzyna:
    def __init__(self , nazwaDruzyny ):
        self.nazwaDruzyny = nazwaDruzyny
        self.czlonkowie = [ Wojownik ]

    def dodajWojownika(self , wojownik):
        self.czlonkowie.append(wojownik)