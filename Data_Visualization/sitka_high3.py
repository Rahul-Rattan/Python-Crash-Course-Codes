from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path=Path("C:/Users/rahul/OneDrive/Desktop/Files/python_works/Data_Visualization/sitka_weather_2021_simple.csv")
lines=path.read_text().splitlines()
reader=csv.reader(lines)
header_row=next(reader)
highs=[]
dates=[]
lows=[]
for index, column_header in enumerate(header_row):
    print(index,column_header)
for row in reader:
    date1=datetime.strptime(row[2],'%Y-%m-%d')
    high=int(row[4])
    low = int(row[5])
    dates.append(date1)
    highs.append(high)
    lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
fig.autofmt_xdate()
plt.show()
