import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[:,::-1])
print(a[::-1])
print()
print(b := np.zeros(2))
print()
print(c := np.zeros([3, 4]))
print()
print(e := np.empty([3, 2])) # empty быстрее чем zeros
print()
print(o := np.ones([2, 3]))
print()
rng = np.random.default_rng(0)
print(rng.random(3))
print()
print(u := np.random.random([3, 4]))