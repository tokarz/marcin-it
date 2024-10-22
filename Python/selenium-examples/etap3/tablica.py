
#tablica
liczby = list(range(1, 21))

#wypisz wszystkie liczby z tablicy ktore sa wieksze od 7
print("Liczby większe od 7:")
for liczba in liczby:
    if liczba > 7:
        print(liczba)

#wypisz wszystkie liczby z tablicy, ktore sa mniejsze od 11
print("Liczby wmniejsze od 11:")
for liczba in liczby:
    if liczba < 11:
        print(liczba)

#parzyste i nieparzyste
def czyParzyste(liczba):
	return liczba %2 ==0

print("Liczby parzyste: ")
for liczba in liczby:
     if czyParzyste(liczba):
          print(liczba)

print("Liczby nieparzyste: ")
for liczba in liczby:
     if not czyParzyste(liczba):
          print(liczba)
    

