from Wojownik import Wojownik
from Druzyna import Druzyna
import random


class Gildia:
    def __init__(self , nazwaGildi , mistrzGildi):
        self.nazwaGildi = nazwaGildi
        self.mistrzGildi = mistrzGildi
        self.druzyny = [Druzyna]

    def dodajDruzyne(self , druzyna):
        self.druzyny.append(druzyna)

    def najsilnieszyWoj(self):
        najsilniejszy = 0
        for druzyna in self.druzyny:
            for wojownik in druzyna.czlonkowie:
                if najsilniejszy is 0 or wojownik.sila > najsilniejszy.sila:
                    najsilniejszy = wojownik
        return najsilniejszy
    
    def najwiekszyLvl(self):
        najwiekszyLvl = 0
        for druzyna in self.druzyny:
            for wojownik in druzyna.czlonkowie:
                if najwiekszyLvl is 0 or wojownik.level > najwiekszyLvl.level:
                    najwiekszyLvl = wojownik
        return najwiekszyLvl
    
gildia = Gildia("Cienie Valhalli" , "Ragnar")

imiona = ["Thorin", "Eldrin", "Gorash", "Liriel", "Azog"]
rasy = ["Elf", "Ork", "Człowiek", "Krasnolud"]
nazwy_druzyn = ["Wilki Północy", "Strażnicy Ognia", "Mroczne Ostrza"]

for nazwa in nazwy_druzyn:
    druzyna = Druzyna(nazwa)
    for i in range(5):
        wojownik =Wojownik(
            random.choice(imiona),
            random.choice(rasy),
            random.randint(1,100),
            round(random.uniform(1.0, 10.0), 2)
            )
        druzyna.dodajWojownika(wojownik)
    gildia.dodajDruzyne(druzyna)
print(f"Najsilniejszy wojownik: {gildia.najsilnieszyWoj()}")
print(f"Wojownik z najwyższym poziomem: {gildia.najwiekszyLvl()}")



