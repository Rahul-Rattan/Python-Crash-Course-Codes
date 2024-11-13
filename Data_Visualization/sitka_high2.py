from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('C:/Users/rahul/OneDrive/Desktop/Files/python_works/Data_Visualization/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

#Extract high temperatures
dates, highs=[],[]
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    high=int(row[4])
    dates.append(current_date)
    highs.append(high)

print(highs)

#plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs, color='red')

#Format plot
ax.set_title("Daily high temperatures")
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()


