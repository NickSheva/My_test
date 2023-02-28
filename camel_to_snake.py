import re
from functools import reduce
def camel_to_snake(name):
    l = ''
    for i in name:
        if i.isupper():
            l += '_' + i.lower()
        else:
            l += i
    yield l.lstrip('_')
    l1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    yield re.sub('([a-z0-9])([A-Z])', r'\1_\2', l1).lower()
    yield reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, name).lower()
    yield ''.join(['_' + i.lower() if i.isupper() else i for i in name])[1:]
name = "MyCodeMyRules"
for i in camel_to_snake(name):
    print(f'{name} = {i}')
print()
