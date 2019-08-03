import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, high and low temperatures from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
        prcp = float(row[header_row.index('PRCP')])
        dates.append(current_date)
        prcps.append(prcp)
        
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(dates, prcps, c = 'red', alpha = 0.5, s = 10)

# Format plot.
plt.title("Daily precipitations on Death Valley - 2018", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("PRCP", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()