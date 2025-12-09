# todo: TO MA BYĆ BEZ FUNKCJI WBUDOWANYCH??? CHYBA ŻART

def konwertuj_na_opis(tab):
    wystapienie = 1
    opis = []
    print(tab)
    for i in range(len(tab) - 1):
        print(f'i={i}, tab[i]={tab[i]}, tab[i+1]={tab[i+1]}')
        if tab[i] == tab[i + 1]:
            wystapienie += 1
        elif i + 1 == len(tab)-1:
            print('to ostatni element')
            wystapienie = 1
            opis.append(wystapienie)
            opis.append(tab[i+1])
        else:
            opis.append(wystapienie)
            opis.append(tab[i])
            wystapienie = 1
        print('')



    return opis


test_tab1 = [1, 1, 3, 2, 2, 2, 1]
print(konwertuj_na_opis(test_tab1))
