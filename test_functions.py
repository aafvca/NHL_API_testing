import json, jmespath
import messages as mg
from urllib.request import urlopen

print("Loading config ...")
executed = False
separator = '==============================================================================='
ts_str = '================================ TEST SUMMARY ================================='

# Function to load the config file
# Input:
# config_file:  The path and name of the configuration file to be loaded
#               The defaullt path is the local directory
#               The configuration file should be a json file    
# Output:
# The config file to be used as a json object
def load_config(config_file):
    with open('config.json', 'r') as f:
        return json.load(f)

# Function to send a GET request and return the response as a json object
# Input:
#       The url string to send a GET request
# Output:
#       response: Is the BODY part of the GET response message, as a json object
#       executed: A flag to acknowledge that the function was executed
def get_response(url):
    with urlopen(url) as response:
        source = response.read()
    response = json.loads(source)
    executed = True
    return response, executed

# Function to find the players that belong to the same team in two different seasons
# Input:
#       roster1, roster2: A python list including the players that were part of the
#                         team
# Output:
#       player_list: A python list that only includes that players that are in both
#                    lists
#       executed: A flag to acknowledge that the function was executed
def find_players(roster1,roster2):
    player_list = []
    for player in roster1:
        if player in roster2:
            player_list.append(player)
    executed = True
    return player_list, executed

# Function to create a single from a nested list and checks if some list values are empty
# It will write the empty values as N/A
# Input: 
#       nested_list: This is the nested list to convert to single list
# Output:
#       single_list: It returns a python single list
#       empty: It returns True if there are empty values on the nested list
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

# Function to find a single attribute in a json response from a list from several requests
# It uses the function get_response to send the GET messages
# It uses single_from_nested function to return a single list
# This function will:
# 1) Construct an url from a prefix, a list of values and a suffix
# 2) Collects the information filtered by api_exp
# 3) Generates a single list from the nested list received as a response
# Input:
#       url_prefix, url_suffix: Are url strings to be used to create the complete url
#       id_list : Is a list of intermediate values that helps to send individual requests
#       api_exp: Is the filter to find the attribute required
# Output:
#       single_list: A list with the attribute values
#       empty: It returns True if there are empty values on the nested list
#       executed: A flag to acknowledge that the function was executed
#       response_state: A flag to acknowledge that the function get_response was executed
def create_list_multiple(url_prefix,id_list,url_suffix,api_exp):
    stat_list = []
    for player in id_list:
        #print(url_prefix + str(player) + url_suffix)
        data, response_state = get_response(url_prefix + str(player) + url_suffix)
        stat_list.append(api_exp.search(data))
    single_list, empty = single_from_nested(stat_list)
    executed = True
    return single_list, empty, executed, response_state

# This function adds all the values in the list, exclude N/A's
# Input:
#       points_list: A list with the values to be added
# Output:
#       number_of_points: The total of the sum operation
#       executed: A flag to acknowledge that the function was executed
def calculate_team_points(points_list):
    number_of_points = 0
    for points in points_list:
        if type(points) == int:
            number_of_points = number_of_points + points
    executed = True
    return number_of_points, executed

# Function to read the response_state from one message and create a comment if successful or not
# Input:
#       response_state1: True if successful False if unsuccessful
#       msg_response_ok: Message to send if response_state is successfull
#       msg_response_nok_preffix, msg_response_nok_suffix, tc_message_label: Will build a failure message
# Output:
#       A printout to show the response state is successful or not
def response_state_single(response_state1, msg_response_ok,msg_response_nok_preffix, msg_response_nok_suffix, tc_message_label):
    if response_state1 == True:
        print(mg.response_ok)
    else:
        print(mg.response_nok_suffix + tc_message_label  + mg.response_nok_preffix)

# Function to read the response_state from two messagea and create a comment if successful or not
# Input:
#       response_state1 and response_state2: True if successful False if unsuccessful
#       msg_response_ok: Message to send if response_state is successfull
#       msg_response_nok_preffix, msg_response_nok_suffix, season1, season2: Will build a failure message if the state is unsuccessful
# Output:
#       A printout to show the response state is successful or not
#def response_state(response_state1, response_state2, msg_response_ok, msg_response_nok_preffix, msg_response_nok_suffix, season1, season2):
#    if response_state1 and response_state2 == True:
#        print(msg_response_ok)
#    else:
#        if response_state1 == False:
#            print(msg_response_nok_preffix + season1  + msg_response_nok_suffix)
#        else:
#            print(msg_response_nok_preffix + season2  + msg_response_nok_suffix)

# Function to WARN about empty values in the json response
# Input:
#       empty1: True or False from create_list_multiple function
# Output:
#       mg.empty_value: Message to WARN about empty values
def empty_value_single(empty1):
    if empty1 == True:
        print(mg.empty_value)

# Function to find empty values in the json response in two messages
#def empty_value(empty1, empty2):
#    if empty1 or empty2 == True:
#        print(mg.empty_value)

# Function to create the PASS message in TC's
# Input:
#       tc_label: The TC identificator
# Output:
#       pass_string: The message to show if the test case pass
def test_pass(tc_label, pass_string):
    print(separator)
    print(tc_label + ' PASS: ' + pass_string)
    print(separator)

# Function to create the FAIL message in TC's
# Input:
#       tc_label: The TC identificator
# Output:
#       fail_string: The message to show if the test case fail
def test_fail(tc_label, fail_string):
    print(separator)
    print(tc_label + ' FAIL: ' + fail_string)
    print('Check '+ tc_label+'.log for more info')
    print(separator)

# Function to generate a Test Summary printout at the end of execution fir Test Suite or individual execution
# Input:
#       t_pass: The number of TC's passed
#       t_fail: The number of TC's failed
#       t_noexec: The number of TC's not executed
def test_summary(t_pass,t_fail,t_noexec):
    print(ts_str)
    print('PASS: ' + str(t_pass) + "\n" + "FAIL: " + str(t_fail) + "\n" + "NOT EXECUTED: " + str(t_noexec))
    print(separator)

# Function to create logfiles for verification, needs a python list of variables to collect
# Input:
#       tc_label: The TC identificator used as the logfile name
# Output:
#       log_info: Is the list of variables included in the logfile for TS purposes
def log_creation(tc_label,log_info):
    f = open(tc_label + '.log', 'w+')
    for key,val in log_info.items():
        f.write(key + " => " + str(val) + "\n")
    f.close()
