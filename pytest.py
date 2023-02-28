from functools import reduce

def camel_to_snake(word):
    s = ''
    for i in word:
        if i.isupper():
            s += '_' + i.lower()
        else:
            s += i
    yield f"for and if:  {s[1:]}"
    yield f"reduce and lambda: {reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, word).lower()}"
    yield ''.join(['_' + i.lower() if i.isupper() else i for i in word]).lstrip('_')

word = "GeeksForGeeks"
tests = camel_to_snake(word)
for test in tests:
    print(test)
def snake_to_camel(word):
    return ''.join([i[0].upper() +i[1:] for i in word.split('_')])



word = "geeks_for_geeks"
print(snake_to_camel(word))
