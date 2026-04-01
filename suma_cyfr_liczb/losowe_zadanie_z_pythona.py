import random

liczby_czterocyfrowe = []
n = 50
for i in range(n):
    liczby_czterocyfrowe.append(random.randint(1000, 9999))

for liczba in liczby_czterocyfrowe:
    liczba = str(liczba)
    if liczba[-1] == '9' or liczba[0] == 6:
        print(liczba)
