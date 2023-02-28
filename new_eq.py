import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime
filename = 'venv/data/new_eq_map.json'
with open(filename) as f:
    new_all_eq = json.load(f)

eq_dicts = new_all_eq['features']
print(len(eq_dicts))
dates, mags, longs, lats = [], [], [], []
for eq in eq_dicts:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    date = datetime.strptime(eq['properties']['time'], '%Y-%m-%d')
    mags.append(mag)
    longs.append(lon)
    lats.append(lat)
    dates.append(date)
print(mags[:5])
print(longs[:5])
print(lats[:5])

data = [{
    'type':'scattergeo',
    'lon':longs,
    'lat':lats,
    'date' : dates,
    'marker' :{ # ключ 'marker', для определения велечины каждого маркера на карте
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'YlGnBu',
        'reversescale' : True,
        'colorbar' : {'title': "Magnitude"}

    }
}]
my_laut = Layout(title  = 'Earth Quake Map')
fig = {'data' : data, 'layout' : my_laut}
offline.plot(fig, filename = 'eq_map.html')