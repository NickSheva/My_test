from plotly.graph_objs import Bar, Layout
from plotly import offline

from random import randint
class Dice():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)

dice = Dice()
results = []
for rollnums in range(100):
	result = dice.roll()
	results.append(result)

#Анализ результатов
frequencies = []
for value in range(1, dice.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)

#визуализация результатов
x_values = list(range(1, dice.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequensy of Result'}

my_layout = Layout(title='Results of rolling one D6 100 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')