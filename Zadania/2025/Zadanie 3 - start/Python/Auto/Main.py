from auto import Auto
from kolo import Kolo
from silnik import Silnik
from kierownica import Kierownica
from skrzynia_biegow import SkrzyniaBiegow


def Main():
    new_Auto = Auto (
        kolo = Kolo(78 , "sredni") , 
        silnik = Silnik(1.9 , "elektryk") , 
        skrzyniaBiegow= SkrzyniaBiegow(5 , True) , 
        kierownica= Kierownica(False)
        )
    print(new_Auto)

Main()
