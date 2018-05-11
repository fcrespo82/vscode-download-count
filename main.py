#!/usr/bin/env python3
import requests
import bs4
import json
from datetime import datetime
import os

extensions = [
    'fcrespo82.rot',
    'fcrespo82.secretlens',
    'fcrespo82.markdown-table-formatter'
]

e = {}
if os.path.exists('extensions.json'):
    with open('extensions.json', 'r+') as json_file:
        e = json.load(json_file)

for ext in extensions:
    url = f'https://marketplace.visualstudio.com/items?itemName={ext}'
    response = requests.get(url)
    parser = bs4.BeautifulSoup(response.content, 'html.parser')
    items = parser.findAll(
        'script', attrs={'class': 'vss-extension'}, recursive=True)
    for item in items:
        extension = json.loads(item.text)
        name = extension['displayName']
        installs = list(
            filter(lambda x: x['statisticName'] == 'install', extension['statistics']))[0]
        downloads = int(installs['value'])
        date = datetime.now().strftime('%Y-%m-%d_%H')
        if not ext in e.keys():
            e[ext] = {'name': name, 'installs': {}}
        if not date in e[ext]['installs']:
            e[ext]['installs'].update({date: downloads})

with open('extensions.json', 'w+') as json_file:
    json.dump(e, json_file, indent=4)
