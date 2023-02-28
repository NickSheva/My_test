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

def checkio(num: int) -> str:
        if num < 20:
            result = (FIRST_TEN + SECOND_TEN)[num - 1]
        elif num < 100:
            result = OTHER_TENS[num // 10 -2]
            if num % 10:
                result += ' ' + checkio(num%10)
        elif num < 1000:
            result = checkio(num // 100) + ' ' + HUNDRED
            if num % 100:
                result += ' ' + checkio(num % 100)
        return result

print("Example:")
#print(checkio(4))
print(checkio(374))


print("The mission is done! Click 'Check Solution' to earn rewards!")
