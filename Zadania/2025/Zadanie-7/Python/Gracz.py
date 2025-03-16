
class Gracz:
    def __init__(self , actualWeapon):
        self.actualWeapon = actualWeapon
    
    def shoot(self):
        if self.actualWeapon:
            self.actualWeapon.shoot()
        else :
            print ("Nie ma broni!")