import re
## Данные
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']
input_ok = lambda x: re.fullmatch('([01][0-9]|2[0-3]):([0-5][0-9])', x) != None
for i in inputs:
  print(input_ok(i))
print()
print('The correct time is:')
print(*[i for i in inputs if input_ok(i)==True], sep='\n')

