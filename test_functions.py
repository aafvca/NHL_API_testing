import json, jmespath
import messages as mg
from urllib.request import urlopen

print("Loading config ...")
executed = False
separator = '==============================================================================='

# Function to load the config
def load_config(config_file):
    with open('config.json', 'r') as f:
        return json.load(f)

# Function to send a GET request and store the response
def get_response(url):
    with urlopen(url) as response:
        source = response.read()
    response = json.loads(source)
    executed = True
    return response, executed

# Function to find the players that worked in both seasons (2016-2017 and 2017-2018)
def find_players(roster1,roster2):
    player_list = []
    for player in roster1:
        if player in roster2:
            player_list.append(player)
    executed = True
    return player_list, executed

# Function to create a single from nested lists and check if some values are empty
def single_from_nested(nested_list):
    single_list = []
    empty = False
    for element in nested_list:
        if len(element) == 0:
            empty = True
            element.append('N/A')
        for points in element:
            single_list.append(points)
    return single_list, empty

#Function to create a list from several requests
def create_list_multiple(url_prefix,id_list,url_suffix,api_exp):
    stat_list = []
    for player in id_list:
        #print(url_prefix + str(player) + url_suffix)
        data, response_state = get_response(url_prefix + str(player) + url_suffix)
        stat_list.append(api_exp.search(data))
    single_list, empty = single_from_nested(stat_list)
    executed = True
    return single_list, empty, executed, response_state

# Function to calculate the team api_points, exclude N/A's
def calculate_team_points(points_list):
    number_of_points = 0
    for points in points_list:
        if type(points) == int:
            number_of_points = number_of_points + points
    executed = True
    return number_of_points, executed

# Function to verify the response message in two GET requests and send ok/not ok message
def response_state(response_state1, response_state2, msg_response_ok, msg_response_nok_preffix, msg_response_nok_suffix, season1, season2):
    if response_state1 and response_state2 == True:
        print(msg_response_ok)
    else:
        if response_state1 == False:
            print(msg_response_nok_preffix + season1  + msg_response_nok_suffix)
        else:
            print(msg_response_nok_preffix + season_1718  + msg_response_nok_suffix)

# Function to find empty values in the json response in two messages
def empty_value(empty1, empty2):
    if empty1 or empty == True:
        print(mg.empty_value)

# Function to create the PASS message
def test_pass(tc_label, pass_string):
    print(separator)
    print(tc_label + ' PASS: ' + pass_string)
    print(separator)

# Function to create the FAIL message
def test_fail(tc_label, fail_string):
    print(separator)
    print(tc_label + ' FAIL: ' + fail_string)
    print('Check '+ tc_label+'.log for more info')
    print(separator)

# Fnction to create logfiles for verification, needs a list of variables to collect
def log_creation(tc_label,log_info):
    f = open(tc_label + '.log', 'w+')
    for key,val in log_info.items():
        f.write(key + " => " + str(val) + "\n")
    f.close()
