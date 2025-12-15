def wczytaj_pi(przyklad=False):
    if przyklad:
        plik = 'pi_przyklad.txt'
    else:
        plik = 'pi.txt'
    with open(plik, 'r') as f:
        dane = f.read().split()
    pi = []
    for i in range(len(dane)):
        pi.append(int(dane[i]))
    return pi


# print(wczytaj_pi(przyklad=True))

pi = wczytaj_pi(przyklad=False)

dwucyfr = []
for i in range(len(pi)):
    if i + 1 == len(pi):
        break
    fragment = int(str(pi[i]) + str(pi[i + 1]))
    dwucyfr.append(fragment)

# print(len(dwucyfr))
licznik = 0
for liczba in dwucyfr:
    if liczba > 90:
        licznik += 1

print(licznik)