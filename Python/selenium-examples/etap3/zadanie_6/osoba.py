class Osoba:
    def __init__(self , imie  , nazwisko , wiek ):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def jedz(self):
        print(f"{self.imie}{self.nazwisko} je")
    
    def pij(self):
        print(f"{self.imie}{self.nazwisko} pije")



class Pilkarz(Osoba):
    def __init__(self, imie , nazwisko , wiek , szybkosc , strzal ):
        super().__init__( imie , nazwisko , wiek )
        self.szybkosc = szybkosc
        self.strzal = strzal

    def graj(self):
        print(f"{self.imie}{self.nazwisko} gra na boisku !")
    def strzelaj(self):
        print(f"{self.imie}{self.nazwisko} strzela bramke!")    

class Bramkarz(Pilkarz):
    def __init__(self , imie , nazwisko , wiek , szybkosc , strzal , wyskok , gra_na_przedpolu ):
        super().__init__( imie , nazwisko , wiek , szybkosc , strzal )
        self.wyskok = wyskok
        self.gra_na_przedpolu = gra_na_przedpolu

    def bron(self):
        print(f"{self.imie}{self.nazwisko} broni pilke")

class Kapitan(Pilkarz):
    def __init__(self, imie, nazwisko, wiek, szybkosc, strzal):
        super().__init__(imie, nazwisko, wiek, szybkosc, strzal)

    def rozmawiaj_z_sedzia(self):
        print(f"{self.imie}{self.nazwisko} rozmawia z sedzia ")

pilkarz1 = Kapitan("Marcin ", "Iskrzycki ", "26 " , "80" , "90" )
pilkarz2 = Bramkarz("Jan ", "Kowalski ", "28 " , "50" , "67" , "wyskok=80" , "przedpole = 88" )
pilkarz3 = Pilkarz("Piotr ", "Zielinski ", "28 " , "88" , "94" )
pilkarz4 = Pilkarz("Robert ", "Lewandowski ", "36 " , "88" , "98" )
pilkarz5 = Pilkarz("Jacek " , "Krzynówek ", "50 " , "100" , "99" )
pilkarz6 = Pilkarz("Michal ", "Pazdan ", "30 " , "78" , "67" )


pilkarz3.graj()
pilkarz5.strzelaj()
pilkarz1.rozmawiaj_z_sedzia()
pilkarz2.bron()
