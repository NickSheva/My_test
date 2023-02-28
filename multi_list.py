a = ["A", "B", "C"]
b = [2, 3, 2]
x = []
for i in range(len(a)):
    x += a[i] * b[i]
print(x)
print()
print([i for i, j  in zip(a, b) for _ in range(j)])
print()
from itertools import repeat, chain
print(*chain(*map(repeat, a, b)))
print()
c = []
for i,j in zip(a, b):
    c.extend(i * j)
print(c)
print()
g = []
for i in range(len(a)):
    g.extend(a[i] * b[i])
print(g)
print()
print(list(map(lambda x, y: [i for i in x] * y, a, b)))

