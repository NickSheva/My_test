import re
def reverse(name):
	return ''.join(reversed(name))


def is_polindrome(name):
    pattern = r'\,|\.|\?|\'|\"|\!|\-|\s'
    p_name = re.sub(pattern, "", name)
    return p_name == reverse(p_name)
n = input().lower()
print(reverse(n))
print('YES' if is_polindrome(n) else 'NO')