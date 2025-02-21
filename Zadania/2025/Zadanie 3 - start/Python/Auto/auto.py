from kierownica import Kierownica
from skrzynia_biegow import SkrzyniaBiegow
from silnik import Silnik
from kolo import Kolo


class Auto:
    def __init__(self , kolo : Kolo , silnik : Silnik , skrzyniaBiegow : SkrzyniaBiegow , kierownica : Kierownica) :
        self.kolo = kolo
        self.silnik = silnik
        self.skrzyniaBiegow = skrzyniaBiegow
        self.kierownica = kierownica