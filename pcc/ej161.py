import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file.
    dates, prcps = [], []
    for row in reader:
        station_name = row[header_row.index('NAME')]
        current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
        prcp = float(row[header_row.index('PRCP')])
        dates.append(current_date)
        prcps.append(prcp)
        
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, prcps, c = 'red', alpha = 0.5, s = 10)

# Format plot.
plt.title(f"Daily precipitations of {station_name} - 2018", fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("PRCP", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()