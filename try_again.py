import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors
for key in colors.PLOTLY_SCALES.keys():
    print(key)
filename = 'venv/data/eq.json'
with open(filename) as f:
    all_eq_dates = json.load(f)
eq_dicts = all_eq_dates['features']
print(len(eq_dicts))
mags, lons, lats, hover_text = [], [], [], []
for eq in eq_dicts:
    mag = eq["properties"]['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    title = eq['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

data = [{'type':'scattergeo', 'lon':lons, 'lat':lats, 'text':hover_text,
         'marker': {'size': [5*mag for mag in mags],
                    'color': mags,
                    'colorscale':'Earth',
                    'reversescale': True,
                    'colorbar': {'title':'Magnitude'}}}]
my_layout = Layout(title = 'EARTHQUAKE MAP')
fig = {'data': data, 'layout':my_layout}
offline.plot(fig, filename = 'eq_dates.html')


