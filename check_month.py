eng = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Dicember']
ru = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
def month(num, lang):
    if 1<=num<=12:
        if lang == 'eng':
            return eng[num - 1]
        else:
            return ru[num - 1]
    else:
        return f"You number {num} isn't wrong. The range from 1 to 12"
num = int(input('Enter number or month: '))
lang = input('Choose language: ')
print(month(num, lang))