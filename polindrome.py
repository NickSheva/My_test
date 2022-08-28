def reverse(name):
	return ''.join(reversed(name))
def is_polindrome(name):
	return name == reverse(name)
s = input()
print('YES' if is_polindrome(s) else 'NO')