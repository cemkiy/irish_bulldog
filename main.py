import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getStatusFightsbyFighter(fighter):
    fighterResponse = urlopen("http://ufc-data-api.ufc.com/api/v1/us/fighters/"+str(fighter["id"])).read()
    soup = BeautifulSoup(fighterResponse, 'html.parser')
    fightsStatuses = soup.findAll("img", { "class" : "fight-result-flag" })

    fighter["statuses"] = []
    for fightsStatus in fightsStatuses:
        fighter["statuses"].append(fightsStatus.get('alt', ''))

def getFighterScore(fighter):
    fighter["score"] = fighter["wins"] - fighter["losses"]
    wins_count = 0
    for status in fighter["statuses"]:
        if status == "win":
            wins_count += 1
        else:
            break
    fighter["score"] += wins_count

    if wins_count > 2 and fighter["title_holder"]:
        fighter["score"] += 2


fightersResponse = urlopen("http://ufc-data-api.ufc.com/api/v1/us/fighters").read().decode('utf8')
fighters = json.loads(fightersResponse)

eventsResponse = urlopen("http://ufc-data-api.ufc.com/api/v1/us/events").read().decode('utf8')
events = json.loads(eventsResponse)
last_event = urlopen("http://ufc-data-api.ufc.com/api/v1/us/events/"+str(events[0]["id"])).read()

soup = BeautifulSoup(last_event, 'html.parser')
reds = soup.findAll("h1", { "class" : "fighter-name-red" })
blues = soup.findAll("h1", { "class" : "fighter-name-blue" })

fights = []
for i in range(0, len(reds)):
    fight = {}
    red_last_name = reds[i].getText()[1:]
    blue_last_name = blues[i].getText()[1:]
    for fighter in fighters:
        if fighter["last_name"] == red_last_name:
            getStatusFightsbyFighter(fighter)
            getFighterScore(fighter)
            fight["red"] = fighter
        elif fighter["last_name"] == blue_last_name:
            getStatusFightsbyFighter(fighter)
            getFighterScore(fighter)
            fight["blue"] = fighter

    fights.append(fight)

for fight in fights:
    red = (fight["red"]["score"]*100)/(fight["red"]["score"]+fight["blue"]["score"])
    blue = (fight["blue"]["score"]*100)/(fight["red"]["score"]+fight["blue"]["score"])
    print(fight["red"]["last_name"] + ":" + str(round(red,2)) + "------" + fight["blue"]["last_name"] + ":" + str(round(blue,2)))
