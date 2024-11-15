from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

path=Path('C:/Users/rahul/OneDrive/Desktop/Files/python_works/Data_Visualization/death_valley_2021_simple.csv')
lines=path.read_text().splitlines()
reader=csv.reader(lines)
header_row=next(reader)

for index, column_header in enumerate(header_row):
    print(index,column_header)

dates, highs, lows = [], [], []

for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high=int(row[3])
        low=int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
print(dates, '\n',highs, '\n', lows)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red')
ax.plot(dates,lows, color='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_title("Highs and lows in Death Valley")
ax.set_xlabel("Dates")
ax.set_ylabel("Temperatures")
fig.autofmt_xdate()
plt.show()