def max_profit(price):
    n = len(price) - 1
    # ciecie = 1, price[1]+price[7]
    # ciecie = 2, price[2]+price[6], price[1]+price[1]+price[6]
    dp = [0] * (n + 1)  # ile mogę maksymalnie dostać za index długości pręta
    for i in range(1, n + 1):
        najlepsza_cena = 0
        # dlugosc = 2 -> price[1] + dp[1], price[2] + dp[0]
        for j in range(1, i + 1):
            najlepsza_cena = max(najlepsza_cena, price[j] + dp[i - j])
        dp[i] = najlepsza_cena
    print(dp)
    return dp[n]


price = [0, 1, 5, 8, 9, 10, 17, 17, 20]

print(max_profit(price))
