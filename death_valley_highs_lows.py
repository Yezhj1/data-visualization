import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"miss data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    
plt.style.use('seaborn')
fig, aix = plt.subplots()
aix.plot(dates, highs, c='red')
aix.plot(dates, lows, c='blue')
aix.fill_between(dates, highs, lows, facecolor='blue')
fig.autofmt_xdate()
plt.show()
