import json
from urllib.request import urlopen

print('Functions loaded')

# Function to load the config
def load_config(config_file):
    with open('config.json', 'r') as f:
        return json.load(f)

# Function to send a GET request and store the response
def get_response(url):
    with urlopen(url) as response:
        source = response.read()
    response = json.loads(source)
    return response

# Function to find the players that worked in both seasons (2016-2017 and 2017-2018)
def find_players(roster1,roster2):
    player_list = []
    for player in roster1:
        if player in roster2:
            player_list.append(player)
    return player_list

#Function to create a list from one request

#Function to create a list from several requests
