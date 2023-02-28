def int_to_roman(num):
    dict_of_known_val = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                         90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ''
    while num > 0:
        for key, value in dict_of_known_val.items():
            while num >= key:
                result += value
                num -= key
    return result
num = 7
print(int_to_roman(num))
print()


def checkio(data):
    base = "I" * data

    base = base.replace("I" * 5, "V")
    base = base.replace("V" * 2, "X")
    base = base.replace("X" * 5, "L")
    base = base.replace("L" * 2, "C")
    base = base.replace("C" * 5, "D")
    base = base.replace("D" * 2, "M")

    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")

    return base
data = 6
print(checkio(data))
print()





