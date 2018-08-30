import test_functions as tf
import json, jmespath
from urllib.request import urlopen

config = tf.load_config('config.json')

api_teams_roster_id = jmespath.compile(config['TEST1']['API_TEAMS_ROSTER_ID'])

# For TEST1
# Get the API response for both rosters 2016-2017 and 2017-2018
# Input:
#       url_team_: The url for the team in the season 2016-2017 and 2017-2018
# Output:
#       roster_data_1617: Roster information for season 2016-2017 and 2017-2018
#       response_state_1617: Flah to indicate the function response_state was executed
def roster_data(url_team):
    roster_data, response_state = tf.get_response(url_team)
    return roster_data, response_state

# Creates a list based in roster id for seasons 2016-2017 and 2017-2018
# Input:
#       roster_data_: Roster information for season 2016-2017 and 2017-2018
# Output:
#       roster_: Python list with the players id for the season specified
def roster_list(roster_data):
    roster_list = api_teams_roster_id.search(roster_data)
    return roster_list

#Finds players that are part of the team in both seasons
# Input:
#       roster_: Python list with the player ID's for both seasons
# Output:
#       players_in_both: A python list with the ID's that are in both lists
#       found_players: A flag to acknowledge that the function was executed
def players_in_both(roster_1, roster_2):
    players_in_both, found_players = tf.find_players(roster_1, roster_2)
    return players_in_both, found_players

# For TEST2
# Reusing players_in_both from TEST1 to collect the points information from people function
# Input:
#       url_people, players_in_both and url_stats: Will create the full url leading to the players stats
#       api_points: The jmespath filter to collect the information needed in this case the players points
# Output:
#       roster_*_points: A python list with the players points
#       collect_1617, response_state_1617: Flags to acknowledge that the function was executed
#       empty_value_1617: An indicator for empty values in the lists
def roster_points(url_people,players_in_both,url_stats,api_points):
    roster_points, empty_value, collect, response_state = tf.create_list_multiple(url_people,players_in_both,url_stats,api_points)
    return roster_points, empty_value, collect, response_state

# Calculate team points based in the roster_points
# Input:
#       roster_*_points: A python list with the individual points per season
# Output:
#       team_points_: A total of the players points in a season
#       calculate_*: Flag to acknowledge that the function was executed
def team_points(roster_points):
    team_points, calculate = tf.calculate_team_points(roster_points)
    return team_points, calculate

# For TEST3
# Using roster_1718 to find if there is a difference between teams and people functions
# Getting the teams using teams functions

# Creates a list based in the team
# Input:
#       url_people,roster_1718,key: Will create the url to the players stats
#       api_people_currentTeam: The jmespath filter to collect the information needed in this case the players currentTeam
# Output:
#       people_current_team: A python list with the team per player
#       t3_collect_current, t3_response_state_current: Flags to acknowledge that the function was executed
#       t3_empty_value_current: An indicator for empty values in the lists
def people_current_team(url_people,roster_1718,key,api_people_currentTeam):
    people_current_team, t3_empty_value_current, t3_collect_current, t3_response_state_current  = tf.create_list_multiple(url_people,roster_1718,key,api_people_currentTeam)
    return people_current_team, t3_empty_value_current, t3_collect_current, t3_response_state_current

# Create a list with the player position using the people function
# Input:
#       url_people,roster_1718,key: Will create the url to the players stats
#       api_people_position: The jmespath filter to collect the information needed in this case the players position
# Output:
#       people_position: A python list with the position per player
#       t3_collect_position, t3_response_state_position: Flags to acknowledge that the function was executed
#       t3_empty_value_position: An indicator for empty values in the lists
def people_position(url_people,roster_1718,key,api_people_position):
    people_position, t3_empty_value_position, t3_collect_position, t3_response_state_position = tf.create_list_multiple(url_people,roster_1718,key,api_people_position)
    return people_position, t3_empty_value_position, t3_collect_position, t3_response_state_position
