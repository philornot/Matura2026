dane = [2,3,5,63,1,3,5,6,1,2,9,3,4,5]
maks = max(dane)
wystapienia = [0] * (maks +1)
posortowana = []

for liczba in dane:
    wystapienia[liczba] += 1

for liczba in range(len(wystapienia)):
    for i in range(wystapienia[liczba]):
        posortowana.append(liczba)

print(posortowana)