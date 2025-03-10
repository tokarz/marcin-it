from Gracz import Gracz
class Terrorysta:
    Gracz = Gracz()
    def __init__(self , actualWeapon):
        super().__init__(actualWeapon)
        self.czyMaBombe = False

    def podlozBombe(self):
        self.czyMaBombe = True
        print("Podklada bobmbe!")

    def changeWeapon(self , newWeapon):
        self.actualWeapon = newWeapon


        
        