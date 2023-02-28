import json
filename = 'venv/data/eq.json'
with open(filename) as f:
    all_eq = json.load(f)

all_dicts = all_eq["features"]
print(len(all_dicts))
mags, lons, lats, hover_text = [], [], [], []
for eq in all_eq:
    mag = eq['"properties"']['mag']
    lon =