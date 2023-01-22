import re
def is_palindrom(n):
    right_n = re.sub("[ ,.;:?!-]", '', n)
    return 'yes' if right_n == right_n[::-1] else 'no'
n = input().lower()
print(is_palindrom(n))