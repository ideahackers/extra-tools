'''
Watches my.hackmit.org for changes in HTML. Use to
detect puzzle upload.

Author: Wyatt Phillips
'''

import requests, bs4
import time, datetime
import os
from pushsafer import init, Client

def print_wtime(text):
    print(datetime.datetime.fromtimestamp(time.time()).strftime('[%Y-%m-%d %I:%M %p]: ') + text)

url = 'https://hackmit.org/'
string_watch = "<!-- nice attempt, but puzzle isn't up yet -->"
update_time = 60

event_fire_attempt = 0
event_fired = False

while not event_fired:

    res = requests.get(url)

    event_fire_attempt = event_fire_attempt + 1

    if not res.status_code == 200:
        print_wtime('failed to retrieve webpage (' + str(res.status_code) + ')... attempt #' + str(event_fire_attempt))
        time.sleep(update_time)
    elif not string_watch in res.text:
        print_wtime('Event Fired: String detected at ' + url)
        event_fired = True
        init("9pF4clfsIC4DQGrQQgul")
        Client("").send_message("A puzzle has ben uploaded to HackMIT!", "Event Fired!", "17746", "26", "5", "3", "https://hackmit.org/", "HackMIT", "0", "1", "120", "1200", "0", "", "", "")
    else:
        print_wtime('no state change detected... attempt #' + str(event_fire_attempt))
        time.sleep(update_time)