x = [1, 2, 3, 4]
print(sum(x)) #=> 10
v = '4, 5, 6'
a = eval('sum([3,4,3])')
print(a)
print()
x = [1.2, 3.4]
print(sum(x)) #=> 4.6
print()
import re
line = '8.3 11 nine 1 5 3 9 five 15 13 7 13.9 number'
find = re.findall(r'[\d\.?,?]+', line)
print(sum(map(float, find)))