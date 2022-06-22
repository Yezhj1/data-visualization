import csv
from shutil import which
import matplotlib.pyplot as plt
from datetime import datetime

# from tomlkit import datetime


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs = [], []
    # print(type(reader))
    for row in reader:
        currunt_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        highs.append(high)
        dates.append(currunt_date)
    
plt.style.use('seaborn')
fig, aix = plt.subplots()
aix.plot(dates, highs, c='red')

aix.set_title("2018.7 highest tempreture per day!", fontsize=24)
aix.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
aix.set_ylabel('tempreture', fontsize=16)
aix.tick_params(axis='both', which='major', labelsize=16)

plt.show()

print(highs)