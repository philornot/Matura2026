suma =int('132',4) + int('3111',4)
odpowiedzi = [int('1111011',2), int('362', 8), int('F3',16), int('3303',4)]
for i, odp in enumerate( odpowiedzi):
    if odp == suma:
        print(i, odp)
    else:
        print(i)