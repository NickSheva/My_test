eng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',  'september', 'october', 'november', 'dicember']

ru =  ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

def month_num(d, lang):
  if 1<=d<=12:
    if lang == 'eng':
      return eng[d-1].title()
    else:
      return ru[d-1].title()
  else:
    return 'The range of month number is wrong'
    
d = int(input('Enter the number of month: \n'))
lang = input('Enter the language (eng/ru):\n')
print(month_num(d, lang))
