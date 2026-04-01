dane = ['1 2 +',
        '5 7 -',
        '3 5 7 - *',
        '3 5 7 - *',
        '1 2 + 3 5 7 - * +']


def czy_liczba(znak):
    try:
        int(znak)
    except ValueError:
        return False
    return True


for wyrazenie in dane:
    print(f'\n\nWyrażenie: {wyrazenie}')
    stos = []
    wyrazenie = wyrazenie.split()
    n = len(wyrazenie)
    for i in range(n):
        znak = wyrazenie[i]
        if czy_liczba(znak):
            stos.append(znak)
            print(f'liczba: {znak}, stos={stos}')
        else:
            prawy = stos.pop()
            lewy = stos.pop()
            nowe_wyrazenie = f'( {lewy} {znak} {prawy} )'
            print(f'lewy={lewy}, prawy={prawy}, wyrażenie={nowe_wyrazenie}')
            stos.append(nowe_wyrazenie)

    print(f'Wynik={stos[0]}')
