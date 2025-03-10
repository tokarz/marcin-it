class Bron():
    def __init__(self , nazwaBroni , czyAutomat = False):
        self.nazwaBroni = nazwaBroni
        self.czyAutomat = czyAutomat
    def shoot(self):
        if self.czyAutomat:
            print(f"{self.nazwaBroni} RATATAATTATAT!")
        else :
            print(f"{self.nazwaBroni} BOOM!")

