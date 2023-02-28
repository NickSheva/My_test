import re
## Данные
text_1 = "98087 crypto-bot that is trading Bitcoin and  is other currencies is  tthat  is that"
## Однострочник
pattern = re.compile("crypto(.{1,30})coin")
## Результат
print(pattern.findall(text_1))
print(re.findall("crypto(.{1,30})coin", text_1))
print(re.findall("t{2}", text_1))
print(re.findall("that(.{1,2})", text_1))
print(re.findall('[a-z0-9]{5,8}', text_1))
print(re.findall('is{1}', text_1))
print()
print()
v = 'The car is parked in the garage the'
print(re.findall('^[Tt]he', v))
print(re.findall('[Tt]he$', v))
print()
print(re.findall("[c|p|g]ar", v))
print(re.findall('[T|t]he|car',v))
m = 'The fat cat sat on the mat.'
print(re.findall('[f|c|s|m]at\.?', m))
dollar = "The fat cat. sat. on the mat."
print(re.findall('(at\.)', dollar))
print(re.findall('(at\.$)', dollar))
print(re.findall('[T|t]he(?=\sfat)', dollar))
print(re.findall('[T|t]he(?!\sfat)', dollar))
# ?=	Положительный Lookahead
# ?!	Отрицательный Lookahead
# ?<=	Положительный Lookbehind
# ?<!	Отрицательный Lookbehind
print(re.findall('[/The/gi]+', dollar))
#i	Нечувствительность к регистру: делает выражение нечувствительным к регистру.
# g	Глобальный поиск: поиск шаблона во всей строке ввода.
# m	Многострочность: анкер метасимвола работает в каждой строке.
print(re.findall(r'/.[at]/g', dollar))
print(re.findall('/.at(.)?$/gm', dollar))
print(re.findall('(.*at)', dollar)) # жадный поиск
print(re.findall('(.*?at)', dollar))

