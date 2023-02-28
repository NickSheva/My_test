
import re
def checkio(words: str) -> bool:
    # add your code here

    pass



print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
print(checkio("Hello World hello"))
print(checkio("He is 123 man"))

a = 'hello my world'
a = a.split()
counter = []
while len(a) > 0:
    c = a[0]
    if c.isalpha():
        counter.append(c)
    else:
        counter.clear()
    a = a[1:]
print(len(counter) == 3)




