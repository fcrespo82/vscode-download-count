#!/usr/bin/env python3
import requests
import bs4
import json
from datetime import datetime

extensions = [
    'fcrespo82.rot',
    'fcrespo82.secretlens',
    'fcrespo82.markdown-table-formatter'
]


print('Extension,Date,Downloads')
for ext in extensions:
    url = f'https://marketplace.visualstudio.com/items?itemName={ext}'
    response = requests.get(url)
    parser = bs4.BeautifulSoup(response.content, 'html.parser')
    with open(f'response-{ext}.html', 'w') as f:
        f.write(parser.prettify())
    items = parser.findAll('script', attrs= {'class': 'vss-extension'}, recursive=True)
    for item in items:
        extension = json.loads(item.text)
        name = extension['displayName']
        installs = list(filter(lambda x: x['statisticName'] == 'install', extension['statistics']))[0]
        downloads = int(installs['value'])
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{name},{date},{downloads}')
