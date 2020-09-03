import xml.etree.ElementTree as ET
import urllib.request
import ssl
import re
import time
import os


def clear_screen():
    os.system('cls')


def extract(details, team_1, team_2):
    """This Function prints various parameters such as team names and their respective scores.
    details contains details of all matches in xml format.
    In xml formatted data 'title' contains the information that we want to extract
    """
    for everymatch in details:
        target_match = everymatch.find('title').text
        match_status = everymatch.find('description').text
        # team_2 in target_match is not really required in if condition
        if team_1 in target_match and team_2 in target_match:
            """regex expression used to group various elements such as team names and their scores
            and then extract them from target_match
            """
            regex = re.compile(r'^(#.+): (.+) #(.+) vs #(.+): ([0-9]+)-([0-9]+)', re.I)
            match = regex.search(target_match)
            home_team = match.group(3)
            away_team = match.group(4)
            home_score = match.group(5)
            away_score = match.group(6)
            print(f"{home_team} {home_score} - {away_score} {away_team}")
            print(f"Match Status: {match_status}")
            print(f"Home - {home_team}")
            print(f"Away - {away_team}")
            print("CTRL-C to EXIT")


def match_details():
    sport = "basketball"

    # ignore SSL Certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #format the url to create the link
    url = 'http://www.scorespro.com/rss2/live-{}.xml'.format(sport)
    url_input = urllib.request.urlopen(url, context=ctx).read()
    """The following code can be used to look at Xml data to look
    at the structure of data
    data = url_input.decode()
    print(data)
    """
    stuff = ET.fromstring(url_input)
    details = stuff.findall("channel/item")
    return details

if __name__ == '__main__':
    team1 = input("Enter Team 1:\t ").capitalize()
    team2 = input("Enter Team 2:\t ").capitalize()
    print("Press CTRL+C anytime you want to EXIT the Application")
    while True:
        info = match_details()
        clear_screen()
        extract(info, team1, team2)
        time.sleep(30)
