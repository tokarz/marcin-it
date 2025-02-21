from Reka import Reka
from Noga import Noga
from Tulow import Tulow
from Glowa import Glowa


class Czlowiek:
    def __init__(self , rekaPrawa : Reka , rekaLewa : Reka , nogaPrawa : Noga , nogaLewa : Noga , tulow : Tulow , glowa : Glowa):
        self.rekaPrawa = rekaPrawa
        self.rekaLewa = rekaLewa
        self.nogaPrawa = nogaPrawa
        self.nogaLewa = nogaLewa
        self.tulow = tulow
        self.glowa = glowa