import csv
import matplotlib.pyplot as plt
from datetime import datetime
print(plt.style.available)

filename = 'venv/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(date)
        highs.append(high)
        lows.append(low)
    print(highs)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
plt.plot(dates, highs, 'r', alpha=0.3)
plt.plot(dates,lows, 'b', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()
ax.set_title('Daily high and low temperature 2018', fontsize=20)
plt.xlabel('', fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.savefig('square_plot.png', bbox_inches='tight')