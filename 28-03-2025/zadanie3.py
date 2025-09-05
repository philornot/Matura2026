def wczytaj_przedzialy():
    przedzialy = []
    with open('dane3.txt', 'r') as plik:
        for linia in plik:
            linia = linia.strip().split()
            a = int(linia[0])
            b = int(linia[1])
            przedzialy.append((a, b))
    return przedzialy


def zadanie_3_1():
    przedzialy = wczytaj_przedzialy()

    dlugosci = []
    for a, b in przedzialy:
        dlugosc = b - a + 1
        dlugosci.append(dlugosc)

    unikalne_dlugosci = []
    for dlugosc in dlugosci:
        if dlugosc not in unikalne_dlugosci:
            unikalne_dlugosci.append(dlugosc)

    for i in range(len(unikalne_dlugosci)):
        for j in range(i + 1, len(unikalne_dlugosci)):
            if unikalne_dlugosci[i] > unikalne_dlugosci[j]:
                temp = unikalne_dlugosci[i]
                unikalne_dlugosci[i] = unikalne_dlugosci[j]
                unikalne_dlugosci[j] = temp

    return f"najmniejsze różne długości przedziałów: {unikalne_dlugosci[0]} i {unikalne_dlugosci[1]}"


def zadanie_3_2():
    przedzialy = wczytaj_przedzialy()

    dlugosci = []
    for a, b in przedzialy:
        dlugosc = b - a + 1
        dlugosci.append(dlugosc)

    licznik = {}
    for dlugosc in dlugosci:
        if dlugosc in licznik:
            licznik[dlugosc] += 1
        else:
            licznik[dlugosc] = 1

    najczestsza_dlugosc = None
    najwyzszy_licznik = 0

    for dlugosc in licznik:
        ilosc = licznik[dlugosc]
        if ilosc > najwyzszy_licznik or (ilosc == najwyzszy_licznik and dlugosc > najczestsza_dlugosc):
            najczestsza_dlugosc = dlugosc
            najwyzszy_licznik = ilosc

    return f"najcześciej występująca długość przedziału: {najczestsza_dlugosc}"


def zadanie_3_3():
    przedzialy = wczytaj_przedzialy()

    def zawiera_sie(p1, p2):
        a1, b1 = p1
        a2, b2 = p2
        return a2 <= a1 and b1 <= b2

    przedzialy_posortowane = []
    for p in przedzialy:
        przedzialy_posortowane.append(p)

    for i in range(len(przedzialy_posortowane)):
        for j in range(i + 1, len(przedzialy_posortowane)):
            if przedzialy_posortowane[i][1] - przedzialy_posortowane[i][0] > przedzialy_posortowane[j][1] - \
                    przedzialy_posortowane[j][0]:
                temp = przedzialy_posortowane[i]
                przedzialy_posortowane[i] = przedzialy_posortowane[j]
                przedzialy_posortowane[j] = temp

    najdluzsze_lancuchy = []
    for i in range(len(przedzialy_posortowane)):
        najdluzsze_lancuchy.append(1)

    for i in range(len(przedzialy_posortowane)):
        for j in range(i):
            if zawiera_sie(przedzialy_posortowane[j], przedzialy_posortowane[i]):
                if najdluzsze_lancuchy[i] < najdluzsze_lancuchy[j] + 1:
                    najdluzsze_lancuchy[i] = najdluzsze_lancuchy[j] + 1

    najdluzszy_lancuch = najdluzsze_lancuchy[0]
    for dlugosc in najdluzsze_lancuchy:
        if dlugosc > najdluzszy_lancuch:
            najdluzszy_lancuch = dlugosc

    return f"długość najdłuższego łańcucha przedziałów: {najdluzszy_lancuch}"


print(zadanie_3_1(),'\n')
print(zadanie_3_2(),'\n')
print(zadanie_3_3())
