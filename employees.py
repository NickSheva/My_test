# данные
employees = {'Ильин' : 100000,
             'Иванов' : 99500,
             'Сидоров' : 123000,
             'Петров' : 88000,
             'Федоров' : 93000}


top_earns = [(k, v) for k, v in employees.items() if v >= 100000]  # выясняем у кого доход выше 100000
print(top_earns)
print()
sort_earns = [dict(sorted(employees.items(), key=lambda item: item[1]))] # сортировка от минимальной суммы до максимума
print(f'{sort_earns}\n')


from operator import itemgetter

sort_surname = [dict(sorted(employees.items(), key=itemgetter(0)))] # др. способ только по имени с itemgetter
print(sort_surname)
