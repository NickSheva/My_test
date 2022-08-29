# Зависимости 
from sklearn.neighbors import KNeighborsRegressor
import numpy as np 
## Данные (площадь дома (в квадратных метрах) / цена квартиры в ЖК КЛЕВЕР ПАРК) 
X = np.array([[35, 5_209_000], 
              [32, 4_900_000], 
              [31, 5_680_000],  
              [32, 5_900_000], 
              [33, 6_200_000], 
              [35, 5_000_000]]) 
## Однострочник 
KNN=KNeighborsRegressor(n_neighbors=3).fit(X[:,0].    
reshape(-1,1), X[:,1]) 
## Результат 
res = KNN.predict([[31]]) 
print(res)
