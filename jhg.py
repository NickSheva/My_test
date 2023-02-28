
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"

def checkio(i):
    if i < 20:
        result = (FIRST_TEN + SECOND_TEN)[i -1]

    elif i < 100:
        result = OTHER_TENS[i // 10]
        if i % 10:
            result += ' ' + checkio(i % 10)
    elif i < 1000:
        result = checkio(i // 100) + ' hundred'
        if i % 100:
            result += ' ' + checkio(i % 100)
    return result

i = 34
print(checkio(i))

