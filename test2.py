from functools import reduce
def column_number(name: str) -> int:
    # your code here
    num = 0
    for c in range(len(name)):
        num = num * 26 + ord(name[c]) - 64
    return num



print("Example:")
print(column_number('AA'))
#column_number("AA")