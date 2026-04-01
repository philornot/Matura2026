import random

n = 20
liczby_pieciocyfrowe = []
for i in range(n):
    liczby_pieciocyfrowe.append(random.randint(10000,99999))

for liczba in liczby_pieciocyfrowe:
    liczba = str(liczba)
    suma = int(liczba[1]) + int(liczba[2]) + int(liczba[3])
    print(f'Suma cyfr środkowych liczby {liczba} to {suma}')