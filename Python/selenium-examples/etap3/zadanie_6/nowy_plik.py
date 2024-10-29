from lib.auto_czesci import Standard
from lib.auto_czesci import Typ
from lib.auto_czesci import Silnik
from lib.auto_czesci import Nr_rejestracyjny
from lib.auto_czesci import Auto




standard = Standard ("wysoki ")
typ = Typ("suv ")
silnik = Silnik("99")
rejestracja = Nr_rejestracyjny("RJS", "1234 ")
auto = Auto(silnik , rejestracja , typ, standard )

auto.pokaz_moc_silnika()

standard2 = Standard("niski")
typ2 = Typ("sedan ")
silnik2 = Silnik("65")
rejestracja2 = Nr_rejestracyjny("KGR" , "3323 ")
auto2 = Auto(silnik2 , rejestracja2 , typ2, standard2)


auto2.pokaz_moc_silnika()