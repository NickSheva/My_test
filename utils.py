from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

import json
import requests


def get_data_from_json_file():
    with open('venv/data/new.json') as f:
        return json.load(f)

def get_questoons_data_by_requests():
    url = get_data_from_json_file()['eq']
    response = requests.get(url)
    return response.json()
