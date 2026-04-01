dane = ['4 * 3 + 2',
        '4 + 3 * 2',
        '1 * ( 2 + 3 ) / 4',
        '4 - 5 ^ ( 3 * 1 ) + 6',
        '1 + 2 / 3 * 4 ^ 5',
        '3 - 2 ^ 4 ( 4 / ( 5 + 6 ) ) * 1',
        '( 8 + 7 * 9 ) ^ ( 7 + ( 1 / 2 ) )']


def czy_liczba(znak):
    try:
        int(znak)
    except ValueError:
        return False
    return True


def onp(wyrazenie):
    wyjscie = []
    stos = []
    priorytety = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    for znak in wyrazenie.split():
        if czy_liczba(znak):
            wyjscie.append(znak)
        elif znak == '(':
            stos.append(znak)
        elif znak == ')':
            while stos[-1] != '(':
                wyjscie.append(stos.pop())
            stos.pop()  # tutaj usuwamy '('
        elif znak in ['^', '*', '/', '+', '-']:
            while stos and stos[-1] != '(' and priorytety[stos[-1]] >= priorytety[znak]:
                wyjscie.append(stos.pop())
            stos.append(znak)

    for i in stos:
        wyjscie.append(i)

    wynik = ''
    for i in wyjscie:
        wynik += i + ' '
    return wynik


for i in dane:
    print(f'{i} --> {onp(i)}')
