plik = open('napisy.txt')
licznik = 0
tablica = []
def wynik_palindrom(wyraz):
    return wyraz == wyraz[::-1]

for linia in plik:
    linia = linia.strip()
    tablica.append(linia)


#KAJAK
#1. KAJAKK
#2. KKAJAK
wynik = ''
for slowo in tablica:
    pierwsza_modyfikacja = slowo + slowo[0]
    druga_modyfikacja = slowo[-1] + slowo
    if wynik_palindrom(pierwsza_modyfikacja) == True:
        wynik = wynik + pierwsza_modyfikacja[25]
    if wynik_palindrom(druga_modyfikacja) == True:
        wynik = wynik + druga_modyfikacja[25]

print(wynik)

