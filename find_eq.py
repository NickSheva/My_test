import json
filename = 'venv/data/eq.json'
with open(filename) as f:
    all_eq = json.load(f)

realabel_file = 'data/eq1.json'
with open(realabel_file, 'w') as r:
    json.dump(all_eq, r, indent=4)
