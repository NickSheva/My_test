import re
def is_polindrome(n):
	pattern = r'\'|\"|\.|\s|\,|\!|\-|\?|\:|\s|\–'
	new_n = re.sub(pattern, '', n.lower())
	return 'YES' if new_n == new_n[::-1] else 'NO'

n = input()
# вызываем функцию
print(is_polindrome(n))