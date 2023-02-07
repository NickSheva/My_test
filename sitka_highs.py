import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)


    for index, column_row in enumerate(header_row):
        print(index, column_row)
# чтение дат и максимальный  и минимальной температур из файла
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # print(highs)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5) # степень прозрачности линий стоновятся более прозрачный
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) # facecolor определяет цвет закрашиваемой области
plt.title('Daily high and low temperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate() # выводит метки дат по диагонали на оси x, чтобы они не перекрывались
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)


plt.show()
from datetime import datetime
d = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(d)

