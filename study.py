import numpy as np
sat_score = np.array([1100, 1250, 1543, 1043, 989, 1412, 1343])
students = np.array(['John', 'Bob', 'Alice', 'Joe', 'Jane', 'Franck', 'Carl'])
top_2 = students[np.argsort(sat_score)[:-3:-1]] # выводим двух студентов набравших больше баллов
print(top_2)
print()
sort_1 = dict(zip(students, sat_score)) # обьединяем фамилии студентов и их баллы в словарь
print(sort_1)
print()
sort_2 = dict(sorted(sort_1.items(), key=lambda item: item[1])) # сортирум словарь по баллам
print(sort_2)








