import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename = 'venv/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_dates = json.load(f)

all_eq_dicts = all_eq_dates['features']
print(len(all_eq_dicts))
mags, longs, lats = [], [], []
for eq in all_eq_dicts:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)

print(mags[:5], longs[:4], lats[:4])

data = [{'type':'scattergeo', 'lon':longs, 'lat':lats}]
my_layout = Layout(title =  'Earth quake map')
fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename='earth quake map.html')

