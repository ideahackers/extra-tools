'''
Watches my.hackmit.org for changes in HTML. Use to
detect puzzle upload.

Author: Wyatt Phillips
'''

import requests, bs4
import time, datetime
import os

def print_wtime(text):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('[%Y-%m-%d %I:%M %p]: ') + text)

url = 'https://hackmit.org/'
string_watch = "<!-- nice attempt, but puzzle isn't up yet -->"
update_time = 5

event_fire_attempt = 0
event_fired = False

that_text = "nope"

while not event_fired:

    try:
        that_text = os.environ['THAT_TEXT']
        break
    except:
        print('Warning: Not all environmental vars are set.')

    res = requests.get(url)

    event_fire_attempt = event_fire_attempt + 1

    if not res.status_code == 200:
        print_wtime('failed to retrieve webpage (' + str(res.status_code) + ')... attempt #' + str(event_fire_attempt))
        time.sleep(update_time)
    elif not string_watch in res.text:
        event_fired = True
        print_wtime('Event Fired: String detected at ' + url)
    else:
        print_wtime('no state change detected... attempt #' + str(event_fire_attempt) + ' .. ' + that_text)
        time.sleep(update_time)