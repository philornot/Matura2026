with open('napisy.txt') as plik:
    napisy = plik.read().split()

maks_dlugosc = 0
for napis in napisy:
    if len(napis) > maks_dlugosc:
        maks_dlugosc = len(napis)

for pozycja in range(maks_dlugosc - 1, -1, -1):

    wystapienia = [0] * 256
    wynik = [None] * len(napisy)

    for napis in napisy:
        if pozycja < len(napis):
            litera = ord(napis[pozycja])
        else:
            litera = 0
        wystapienia[litera] += 1

    for i in range(1, len(wystapienia)):
        wystapienia[i] += wystapienia[i-1]

    for i in range(len(napisy) - 1, -1, -1):
        napis = napisy[i]

        if pozycja < len(napis):
            litera = ord(napis[pozycja])
        else:
            litera = 0

        wystapienia[litera] -= 1
        wynik[wystapienia[litera]] = napis

    napisy = wynik

for napis in napisy:
    print(napis)

# to napisał chatgpt i tego nie rozumiem