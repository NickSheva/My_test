import numpy as np
def num(a, b):
    n = np.product([a, b])
    return n
a = 6
b = 8
print(num(a, b))

def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6 and any(i.isdigit() for i in password)


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
print(is_acceptable_password("short")) #== False
print(is_acceptable_password("muchlonger"))#== False
print(is_acceptable_password("ashort"))# == False
print(is_acceptable_password("muchlonger5"))#== True
print(is_acceptable_password("sh5"))