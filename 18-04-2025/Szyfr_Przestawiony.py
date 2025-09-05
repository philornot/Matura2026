def szyfruj(tekst):
    slowa = tekst.split()
    zaszyfrowane_slowa = ""

    for i in range(len(slowa)):
        slowo = slowa[i]
        zaszyfrowane_slowo = ""
        j = 0
        while j < len(slowo):
            if j + 1 < len(slowo):
                zaszyfrowane_slowo += slowo[j + 1] + slowo[j]
                j += 2
            else:
                zaszyfrowane_slowo += slowo[j]
                j += 1

        zaszyfrowane_slowa = zaszyfrowane_slowa + zaszyfrowane_slowo
        if i < len(slowa) - 1:
            zaszyfrowane_slowa += " "

    return zaszyfrowane_slowa


def deszyfruj(tekst):
    return szyfruj(tekst)


tekst = input('Wprowadź tekst do zaszyfrowania: ')
# tekst = "pies"
# tekst = "samochód"
zaszyfrowany = szyfruj(tekst)
odszyfrowany = deszyfruj(zaszyfrowany)

print("zaszyfrowany:", zaszyfrowany)
print("odszyfrowany:", odszyfrowany)
