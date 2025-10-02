def zapisz_dane(odp1='', odp2='', odp3='', odp4=''):
    with open('wyniki4.txt', 'w') as f:
        f.write(f'Zadanie 4.1: {odp1}\n'
                f'Zadanie 4.2: {odp2}\n'
                f'Zadanie 4.3: {odp3}\n'
                f'Zadanie 4.4: {odp4}')

from zadanie4_1 import odpowiedz1
from zadanie4_2 import odpowiedz2
from zadanie4_3 import odpowiedz3
zapisz_dane(odpowiedz1, odpowiedz2, odpowiedz3)