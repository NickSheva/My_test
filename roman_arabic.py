numbers = dict(M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1)
def to_roman(num):
    roman = ""
    while num > 0:
        for k, v in numbers.items():
            while num >= v:
                roman += k
                num -= v
    return roman
num = int(input())
print(to_roman(num))
def to_arabic(num):
    dec=0
    for k, v in numbers.items():
        while num.startswith(k):
            dec += v
            num = num[len(k):]
    return dec
num = input()
print(to_arabic(num))



