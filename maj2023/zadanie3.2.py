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

pi = wczytaj_pi(przyklad=False)

dwucyfr = []
for i in range(len(pi)):
    if i + 1 == len(pi):
        break
    fragment = str(pi[i]) + str(pi[i + 1])
    dwucyfr.append(fragment)

mozliwe_dwucyfr = []
for i in range(10):
    for j in range(10):
        fragm = str(i)+ str(j)
        mozliwe_dwucyfr.append(fragm)

wystepowania = {}
for moz_d in mozliwe_dwucyfr:
    wystepowania[moz_d] = 0
    for d in dwucyfr:
        # print(moz_d, d)
        if d == moz_d:
            wystepowania[moz_d] += 1

# print(wystepowania)
maks = 0
maks_dwucyfr = ''
min = 9999999999
min_dwucyfr = ''

for d, wyst in wystepowania.items():
    if wyst > maks:
        maks = wyst
        maks_dwucyfr = d
    if wyst < min:
        min = wyst
        min_dwucyfr = d

print(f'{min_dwucyfr} {min}')
print(f'{maks_dwucyfr} {maks}')
