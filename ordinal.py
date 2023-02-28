from num2words import num2words
print(num2words(10, to='ordinal'))#==>tenth
print(num2words(10, to='cardinal'))#==> ten
print(num2words(10, to='ordinal_num'))#==>10th
print(num2words(1054, to='year'))#==> ten
print(num2words(10, to='currency'))#==> zero euro, ten cents
print(num2words(10, lang='ru'))#==>десять
print(num2words(19, lang='ru', to='ordinal'))#==> десятый
