from plotly.graph_objs import Bar, Layout
from plotly import offline

from random import randint
class Dice():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

dice1 = Dice()
dice2 = Dice()
# моделируем серию бросков
results = []
for _ in range(100):
    result = dice1.roll() + dice2.roll()
    results.append(result)
#print(results)
# анализ результатов
frequencies = []
max_result = dice1.num_sides + dice2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title' :'Result',  'dtick': 1}
y_axis_config = {"title" : 'Frequency of results'}

my_layout = Layout(title = 'Result of rolling one d6 100 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename='d6_d6.html')
