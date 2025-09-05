def wczytaj_prostokaty():
    prostokaty = []
    with open('prostokaty.txt', 'r') as plik:
        for linia in plik:
            linia = linia.strip().split()
            h = int(linia[0])
            s = int(linia[1])
            prostokaty.append((h, s))
    return prostokaty


def zadanie_4_1():
    prostokaty = wczytaj_prostokaty()

    pola = []
    for h, s in prostokaty:
        pole = h * s
        pola.append(pole)

    najmniejsze_pole = pola[0]
    for pole in pola:
        if pole < najmniejsze_pole:
            najmniejsze_pole = pole

    najwieksze_pole = pola[0]
    for pole in pola:
        if pole > najwieksze_pole:
            najwieksze_pole = pole

    with open('wyniki4.txt', 'w') as wyniki:
        wyniki.write("-- Zadanie 4.1 --\n")
        wyniki.write(f"{najmniejsze_pole} {najwieksze_pole}\n\n")

    return f"najmniejsze pole: {najmniejsze_pole}, największe pole: {najwieksze_pole}"


def zadanie_4_2():
    prostokaty = wczytaj_prostokaty()

    def miesci_sie(p2, p1):
        h2, s2 = p2
        h1, s1 = p1
        return h2 <= h1 and s2 <= s1

    n = len(prostokaty)
    najdluzszy_ciag = []

    for i in range(n):
        aktualny_ciag = [i]
        ostatni = i

        for j in range(i + 1, n):
            if miesci_sie(prostokaty[j], prostokaty[ostatni]):
                aktualny_ciag.append(j)
                ostatni = j

        if len(aktualny_ciag) > len(najdluzszy_ciag):
            najdluzszy_ciag = []
            for x in aktualny_ciag:
                najdluzszy_ciag.append(x)

    dlugosc_ciagu = len(najdluzszy_ciag)

    if dlugosc_ciagu > 0:
        ostatni_prostokat = prostokaty[najdluzszy_ciag[dlugosc_ciagu - 1]]
        ostatni_h, ostatni_s = ostatni_prostokat
    else:
        ostatni_h, ostatni_s = 0, 0

    with open('wyniki4.txt', 'a') as wyniki:
        wyniki.write("-- Zadanie 4.2 -- \n")
        wyniki.write(f"{dlugosc_ciagu} {ostatni_h} {ostatni_s}\n")

    return (f"długość najdłuższego ciągu: {dlugosc_ciagu}\n"
            f"wysokość i szerokość ostatniego prostokąta: {ostatni_h} {ostatni_s}")


print(zadanie_4_1(), '\n')
print(zadanie_4_2())