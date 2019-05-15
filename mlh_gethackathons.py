'''
Fetches all Major League Hacking affiliated
hackathons for a certain year.

Command line example:
python mlh_gethackathons.py <year>

Dependancies: AKA run the command below before running first time.
pip install beautifulsoup4 lxml requests

Author: Wyatt Phillips
'''

YEAR = '2020'  # Type as a string [Ex: '2020']
FOLDER_OUT = 'mlh/'  # Must include slash at end

FETCH_URL = 'https://mlh.io/seasons/na-' + YEAR + '/events'  # No need to change unless broken.

import requests, bs4
import json
import os
import sys

if len(sys.argv) > 1:
    YEAR = sys.argv[1]
    FETCH_URL = 'https://mlh.io/seasons/na-' + YEAR + '/events'

res = requests.get(FETCH_URL)
res.raise_for_status()
webpage = bs4.BeautifulSoup(res.text, "lxml")

events = []
events_html = webpage.select('.event')

# Create Entry
for i in events_html:
    entry = {
        "name": i.select('h3[itemprop="name"]')[0].getText(),
        "dateStart": i.select('meta[itemprop="startDate"]')[0].get('content'),
        "dateEnd": i.select('meta[itemprop="endDate"]')[0].get('content'),
        "city": i.select('span[itemprop="city"]')[0].getText(),
        "state": i.select('span[itemprop="state"]')[0].getText(),
        "website": i.select('.event-link')[0].get('href'),
        "backdrop": i.select('.image-wrap')[0].select('img')[0].get('src'),
        "icon": i.select('.event-logo')[0].select('img')[0].get('src')
    }
    events.append(entry)

try:
    fileout = FOLDER_OUT + 'mlh-' + YEAR + '.json'
    if not os.path.exists(FOLDER_OUT):
        os.makedirs(FOLDER_OUT)
    with open(fileout, 'w') as outfile:
        json.dump(events, outfile, indent=4, sort_keys=True)
except IOError:
    print('Error: Cannot write to ' + fileout)