import json, jmespath
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

#Function to create a list from several requests
def create_list_multiple(url_prefix,id_list,url_suffix,api_exp):
    stat_list = []
    for player in id_list:
        data = get_response(url_prefix + str(player) + url_suffix)
        stat_list.append(api_exp.search(data))
    return stat_list

# Function to create a single from nested lists and check if some values are empty
def single_from_nested(nested_list):
    single_list = []
    for element in nested_list:
        if len(element) == 0:
            empty = True
            element.append('N/A')
        for points in element:
            single_list.append(points)
    if empty == True:
        print('Warning, there are some empty values in the API, maybe a bug?')
    return single_list

# Function to calculate the team api_points, exclude N/A's
def calculate_team_points(points_list):
    number_of_points = 0
    for points in points_list:
        if type(points) == int:
            number_of_points = number_of_points + points
    return number_of_points
