import csv
from matplotlib import pyplot as plt
from datetime import datetime
print(plt.style.available)
filename = 'data/chicago.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = int(row[6])
        low = int(row[8])
        highs.append(high)
        dates.append(current_date)
        lows.append(low)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, 'r', alpha=0.3)
ax.plot(dates, lows, 'b', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.06)

plt.title('Daily high and low temperature.\n Chicago 2022', fontsize=20)
plt.xlabel('', fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12)
plt.ylim(-20, 120)

plt.show()




