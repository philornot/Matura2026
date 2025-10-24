from zad4_2 import licznik as odp4_2

def zapisz_odp(*odpowiedzi):
    plik = 'wyniki4.txt'
    odpowiedz_koncowa = ''
    numer_zadania = 1
    for odpowiedz in odpowiedzi:
        odpowiedz_koncowa += f'Zadanie {numer_zadania}: {odpowiedz}\n'
        numer_zadania += 1
    with open(plik, 'w') as f:
        f.write(odpowiedz_koncowa)

zapisz_odp(odp4_2)