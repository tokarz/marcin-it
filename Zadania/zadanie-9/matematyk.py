from kalkulator import Kalkulator




class Matematyk:
	def __init__(self):
		self.kalkulator = Kalkulator()

	def policz_dzialanie(self , dzialanie : str):
		wynik = 0
		liczba = ""
		znak = None

		for znak in dzialanie:
			if znak == '+':
				wynik = self.kalkulator.dodaj(wynik , liczba)
			if znak == '-':
				wynik = self.kalkulator.odejmij(wynik , liczba)
			if znak == '*':
				wynik = self.kalkulator.pomnoz(wynik , liczba)
			if znak == '/':
				wynik =	self.kalkulator.podziel(wynik , liczba)

matematyk = Matematyk()

matematyk.policz_dzialanie("1" + "1" / "4")
