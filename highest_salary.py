import numpy as np
## Данные: годовые зарплаты в тысячах долларов (за 2017, 2018 и 2019 гг.)
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])
                     
max_income = np.max(salaries - salaries * taxation)
## Результат
print(max_income)
