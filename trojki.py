# a^2 + b^2 = c^2
# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2
# a, b - przyprostątne
# c - przeciwprostątna
# => a + b > c
def najwiekszy_wspolny_dzielnik(liczba_a, liczba_b):
    while liczba_b != 0:
        liczba_a, liczba_b = liczba_b, liczba_a % liczba_b
    return liczba_a


trojki_pitagorejskie = []

for m in range(2, 20):
    for n in range(1, m):

        # warunki na trójkę pierwotną
        if najwiekszy_wspolny_dzielnik(m, n) != 1:
            continue
        if m % 2 == 1 and n % 2 == 1:
            continue

        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2

        # ujednolicenie kolejności boków
        if a > b:
            a, b = (
                b,
                a
            )

        trojki_pitagorejskie.append(
            (a, b, c)
        )

for trojka in trojki_pitagorejskie:
    print(trojka)
