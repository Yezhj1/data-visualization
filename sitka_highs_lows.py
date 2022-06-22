import matplotlib.pyplot as plt
import csv
from datetime import datetime
# from matplotlib.font_manager import __rebuild
# __rebuild()

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
plt.style.use('seaborn')
fig, aix = plt.subplots()
aix.plot(dates, highs, c='red', alpha=0.5)
aix.plot(dates, lows, c='blue', alpha=0.5)
aix.fill_between(dates, highs, lows, facecolor='blue', alpha=0.4)
aix.set_title("2018年每日最高温度", fontsize=24)
aix.set_ylabel('tempreture', fontsize=16)
aix.set_xlabel('data', fontsize=16)
fig.autofmt_xdate()

plt.show()