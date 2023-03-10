
# На вход программе поступает строка, ваша задача удалить из нее все символы «w» и «z».

s = 'Zlifezzw'.lower()
print(s.replace('w','').replace('z',''))
print()

b = {'z':'', 'w':''}
for k, v in b.items():
    s = s.replace(k, v)
print(s)
print()
import re
pattern = '[w,z]'
print(re.sub(pattern, '', s))

