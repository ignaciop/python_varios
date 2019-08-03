import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, high and low temperatures from this file.
    lats, lons, brightness = [], [], []
    for row in reader:
        try:
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"Missing data")
        else:
            lats.append(lat)
            lons.append(lon)
            brightness.append(bright)
        
lats = lats[:100]
lons = lons[:100]
brightness = brightness[:100]

# Plot the high and low temperatures.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'color': brightness,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Fires'},
    },
}]
my_layout = Layout(title = "Global Fires for 1 day")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_fires.html')