import math
print(f'The value of pi is approximately {round(math.pi, 3)}')
print()
print(f'The value of pi is approximately {math.pi:.3f}')
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name!r} ==> {phone}')

a = '3.14'
print(a.zfill(6))
import datetime
today = datetime.datetime.now()
print(today)
print(str(today))
print(repr(today))