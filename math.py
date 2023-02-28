def nums(a, b):
    yield f"{a} * {b} = {a*b}"
    yield f"{a} / {b} = {round(a/b, 2)}"
    yield f"{a} + {b} = {a+b}"
    yield f"{a} - {b} = {a-b}"
a, b = 10,2
for i in nums(a,b):
    print(i)

