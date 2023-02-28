nums = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)

def roman(d):
    n = ''
    while d > 0:
        for key, value in nums.items():
            while d >= value:
                n += key
                d -= value
    return n
d = 8
print(roman(d))

def arabic(s):
    dig = 0
    for key, value in nums.items():
        while s.startswith(key):
            dig += value
            s = s[len(key):]

    return dig
s = 'III'
print(arabic(s))


