from num2words import num2words
num = 45
print(num2words(num))
print(num2words(num, to = 'ordinal'))
print(num2words(num, to = 'ordinal_num'))
print(num2words(num, to = 'year'))
print(num2words(num, to = 'currency'))
print(num2words(num, lang='ru'))

def num_words(d):
    try:
        return num2words(d, lang='lj')
    except NotImplementedError:
        return num2words(d, lang = 'ru')
d = int(input())
print(num_words(d))