# создать на основе имеющихся данных новую обучающую выборку: каждое второе значение с плавающей точкой. 

price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
sample = [i[::2] for i in price]
print(sample)
print()
import numpy as np
price = np.array([[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]])
         
print(price[:,::2])

# цель заменить каждое второе строковое значение на непосредственно предшествующее ему 
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted', 'Safari', 'corrupted', 'Safari', 'corrupted','Chrome', 'corrupted', 'Firefox', 'corrupted']
visitors[1::2] = visitors[::2]
print(visitors)
            



