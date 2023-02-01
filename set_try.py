def add_to_set1(a, b):
    a.update(b)
    return a
def add_to_set2(a, b):
    a = a.union(b)
    return a
a = { "a", "b" , "c" }
b = { "a", "c", "d" }
print(add_to_set1(a, b))
print(add_to_set2(a, b))
print()
a = { "a", "b" , "c" }
b = { "a", "c", "d" }
print({*a, *b})
print()
a = { "a", "b" , "c" }
a.remove("b")
assert a == { "a", "c" }
print()
a = { "a", "b" , "c" } 
a.difference_update("ab")
print(a == { "c" })

a = { "a", "b" , "c" } 
a.difference_update(["ab"])
print(a == { "a", "b", "c" })
# Оператор -, эквивалент метода .difference(),
# не модифицирует исходный объект
a = { "a", "b" , "c" } 
b = a - { "b", "c" }
print(a != b and b == { "a" })
print()
a = { "a", "b", "c" }
b = { "b", "c", "d" }
print(a & b == { "b", "c" })
print(a.intersection(b) == { "b", "c" })
print()
a = { "a", "b", "c" }
b = { "b", "c", "d" }
print(a ^ b == { "a", "d" })
print(a.symmetric_difference(b) == {"a", "d"})

a = { "a", "b", "c" }
b = { "a", "b" }
print(a.issubset(b) == (a <= b) == False)
print(b.issubset(a) == (b <= a) == True)

