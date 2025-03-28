
class Pilkarz:
    def __init__(self, imie, nazwisko, pozycja, wiek, overall):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pozycja = pozycja
        self.wiek = wiek
        self.overall = overall
    def kopnijPilke(self):
        print(f"{self.imie} {self.nazwisko} kopnij piłkę!")

    def biegnij(self):
        print(f"{self.imie} {self.nazwisko} biegnij!")

    def strzel(self, kierunek):
        print(f"{self.imie} {self.nazwisko} strzelaj! {kierunek}!")

    def przedstawSie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}, gram na pozycji {self.pozycja}, mam {self.wiek} lat.")

pilkarze = [
    Pilkarz("Marcin ", "Iskrzycki ", "napastnik ", "25 ", "99"),
    Pilkarz("Jan ", "Kowalski ", "bramkarz ", "28 ", "78"),
    Pilkarz("Piotr ", "Zielinski ", "pomocnik ", "28 ", "90"),
    Pilkarz("Robert ", "Lewandowski ", "napastnik ", "36 ", "99"),
    Pilkarz("Jacek " , "Krzynówek ", "napastnik ", "50 ", "100"),
    Pilkarz("Michal ", "Pazdan ", "obronca ", "30 ", "76")
    ]



for pilkarz in pilkarze:
    pilkarz.przedstawSie()
    pilkarz.biegnij()
    pilkarz.kopnijPilke()
    pilkarz.strzel("prawy róg")
    print()