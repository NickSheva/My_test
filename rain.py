import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_row in enumerate(header_row):
        print(index, column_row)

    dates, rains = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(date)
        rains.append(rain)
    print(rains)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue', alpha=0.3)
plt.title('Daily presipitation in Sitka -2018', fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Amount of presipitaion', fontsize=14)
plt.show()