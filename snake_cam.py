s = 'MyCamelYour'
l = ''
for i in s:
    if i.isupper():
        l += '_' + i.lower()
    else:
        l += i
print(l[1:])


from functools import reduce
a = reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, s).lower()
print(a)