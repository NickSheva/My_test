n = 'Hello'

while len(n) > 0:
    print(n[0])
    n = n[1:]
print()
n = 'HEo78'
while len(n) > 0:
    am = n[0]
    if am>='a' and am<='z':
        print(f'{am} is small letter')
    elif am.isupper():
        print(f'{am} is big letter')
    elif am.isdigit():
        print(f'{am} is a digit')
    else:
        print(f"{am} is sign")

    n = n[1:]
