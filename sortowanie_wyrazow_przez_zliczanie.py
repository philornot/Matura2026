def zamien_wyraz_na_liste_ord(wyraz):
    return [ord(litera) for litera in wyraz]


def zamien_liste_ord_na_wyraz(lista_ord):
    wyraz = ''
    for litera in lista_ord:
        wyraz += chr(litera)
    return wyraz


napis = 'asvbjkducgslsljdihcksjdvbskjgc'

napis_ord = zamien_wyraz_na_liste_ord(napis)
maks = max(napis_ord)
posortowana_ord = []

wystapienia = [0] * (maks + 1)

for litera_ord in napis_ord:
    wystapienia[litera_ord] += 1

for litera in range(len(wystapienia)):
    for i in range(wystapienia[litera]):
        posortowana_ord.append(litera)

posorotowany_napis = zamien_liste_ord_na_wyraz(posortowana_ord)
print(posorotowany_napis)
