import pandas as pd
import numpy as np
df = pd.DataFrame({'Name':['Nick', 'Lara', 'Ulyana'], 'Age':[42, 43, 13], 'City':['Ivdel', 'Lobva', 'Krasnoturinsk']},
                   columns=['Name', 'Age', 'City'], index=[1,2,3])
df.index.name = 'number'
print(df)
df.to_csv('file1.csv', sep="\t")
new_df = pd.read_csv('file1.csv')
print(new_df)

