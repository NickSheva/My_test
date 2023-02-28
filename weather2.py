import csv
from datetime import datetime
from matplotlib import pyplot as plt


def get_weather_date(filename, dates, highs, lows, date_index, high_index, low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
filename = 'venv/data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_date(filename, dates, highs, lows, date_index=2, high_index=5, low_index=6)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, 'r', alpha=0.4)
ax.plot(dates, lows, c='blue', alpha=0.4)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

filename = 'venv/data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_date(filename, dates, highs, lows, date_index=2, high_index=4, low_index=5)


ax.plot(dates, highs, 'r', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

title = 'Daily high and low temperature'
title += "\nSitka and Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.ylim(20, 130)
plt.show()

