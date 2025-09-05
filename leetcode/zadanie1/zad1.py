def longestPalindrome(s):
    poczatek = 0
    dlugosc_max = 0

    for srodek in range(len(s)):
        # jeśli palindrom ma nieparzysta liczbe liter
        lewo = srodek
        prawo = srodek

        while lewo >= 0 and prawo < len(s) and s[lewo] == s[prawo]:
            dlugosc = prawo - lewo + 1
            if dlugosc > dlugosc_max:
                poczatek = lewo
                dlugosc_max = dlugosc
            lewo = lewo - 1
            prawo = prawo + 1

        # jeśli palindrom jest parzysty
        lewo = srodek
        prawo = srodek + 1

        while lewo >= 0 and prawo < len(s) and s[lewo] == s[prawo]:
            dlugosc = prawo - lewo + 1
            if dlugosc > dlugosc_max:
                poczatek = lewo
                dlugosc_max = dlugosc
            lewo = lewo - 1
            prawo = prawo + 1

    return s[poczatek:poczatek + dlugosc_max]

print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("efakajakrgrg"))
print(longestPalindrome("rgernannaewf"))
