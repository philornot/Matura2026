while True:
    liczba = int(input('liczba='))
    while liczba > 0:
        print(liczba % 3,end='')
        liczba //= 3
    print('\n')