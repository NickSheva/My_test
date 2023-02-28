import csv
from matplotlib import pyplot as plt
from datetime import datetime
print(plt.style.available)
filename = 'venv/data/sitka_weather_2018_simple.csv'
filename = 'venv/data/death_valley_2018_simple.csv'
place_name = ''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    data_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')


    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        if not place_name:
            place_name = row[name_index]
        current_date = datetime.strptime(row[data_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, 'r', alpha=0.3)
ax.plot(dates, lows, 'b', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

plt.title('Daily high and low temperature', fontsize=20)

plt.show()






