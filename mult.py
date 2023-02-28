from math import *
def checkio(number: int) -> int:
    # your code here
    n = list(str(number))
    v = prod([int(i) for i in n if i != '0']) # лучше
    a = lambda n : eval("*".join(i for i in str(n) if i != '0'))
    return a(number)


print("Example:")
print(checkio(123405))

