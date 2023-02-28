import pandas as pd
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
              'population': [17.04, 143.5, 9.5, 45.5],
              'square': [2724902, 17125191, 207600, 603628]})
print(df)
print()
print(df['country'])
print()
# Доступ по индексу в DataFrame
df = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
              'population': [17.04, 143.5, 9.5, 45.5],
              'square': [2724902, 17125191, 207600, 603628]},
                   index = ['KZ', 'RU', 'BY', 'UA'])
print(df)
df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
print(df)
print()
# Доступ к строкам по индексу возможен несколькими способами:
# .loc - используется для доступа по строковой метке
print(df.loc['RU'])
print()
# .iloc - используется для доступа по числовому значению (начиная от 0)
print(df.iloc[0])
# Можно делать выборку по индексу и интересующим колонкам:
print(f"\n{df.loc[['UA'], 'square']}")
#  .loc в квадратных скобках принимает 2 аргумента: интересующий индекс, в том числе поддерживается слайсинг и колонки.
print(f"\n{df.loc['KZ':'BY', :]}")
# Фильтровать DataFrame с помощью т.н. булевых массивов:
print(df[df.population > 20])
print(df[df.population > 10][['country', 'square']])
print()
# Кстати, к столбцам можно обращаться, используя атрибут или нотацию словарей Python,
# т.е. df.population и df['population'] это одно и то же.
print(df['population'])
print(df.population)
print()
print(df['population'])
# Сбросить индексы можно вот так:
df.reset_index()
# pandas при операциях над DataFrame, возвращает новый объект DataFrame.
# Добавим новый столбец, в котором население (в миллионах) поделим на площадь страны, получив тем самым плотность
df['density'] = df['population']/ df['square'] * 1000000
print(df)
# Не нравится новый столбец? Не проблема, удалим его:
a = df.drop(['density'], axis='columns')
print(a)
# Особо ленивые могут просто написать del df['density'].
del df['density']
print(df)
# Переименовывать столбцы нужно через метод rename:
df = df.rename(columns={'Country Code': 'country_code'})