a = set('abracadabra') # 'a', 'b', 'r', 'c', 'd'
b = set('alacazam') # 'm', 'a', 'c', 'l', 'z'
print(a - b) # {'b', 'r', 'd'}
print(a | b) # {'a', 'b', 'r', 'c', 'd', 'm', 'l', 'z'}
print(a & b) # {'a', 'c'}
print(a ^ b) # {'b', 'r', 'd', 'm', 'l', 'z'}
print({x for x in 'abracadabra' if x not in ('abc')}) # {'r', 'd'}
print()
print(list('COUNTRY')) # ['C', 'O', 'U', 'N', 'T', 'R', 'Y']
print()
d = 'CAT'
print([j* i for j in range(1, 4) for i in d]) # ['C', 'A', 'T', 'CC', 'AA', 'TT', 'CCC', 'AAA', 'TTT']
print([[i] for i in range(1, 7)]) # [[1], [2], [3], [4], [5], [6]]
print([[i +j for i in range(2, 5)] for j in range(2, 5)]) # [[4, 5, 6], [5, 6, 7], [6, 7, 8]]
print([i ** 2 for i in range(10)]) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()
my_list = [i for i in range(1, 25) for j in range(2)]
print(my_list)
print(len([i for i in my_list if i in (11, 18, 20)]))
print(my_list.count(11))
from collections import Counter
print(Counter(my_list))
print()
test_str = "Pythonist"

count = Counter(test_str)
def sorted_lest(d):
    return True if d == sorted(d) else False
d = [6, 7, 8, 9]
print(sorted_lest(d))
print()
