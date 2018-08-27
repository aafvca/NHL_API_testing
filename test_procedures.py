import test_functions as tf
import json, jmespath
from urllib.request import urlopen

config = tf.load_config('config.json')

api_teams_roster_id = jmespath.compile(config['TEST1']['API_TEAMS_ROSTER_ID'])

# For TEST1
# Get the API response for both rosters 2016-2017 and 2017-2018
def roster_data_1617(url_team_1617):
    roster_data_1617, response_state_1617 = tf.get_response(url_team_1617)
    return roster_data_1617, response_state_1617

def roster_data_1718(url_team_1718):
    roster_data_1718, response_state_1718 = tf.get_response(url_team_1718)
    return roster_data_1718, response_state_1718

# Creates a list based in roster id
def roster_1617(roster_data_1617):
    roster_1617 = api_teams_roster_id.search(roster_data_1617)
    return roster_1617

def roster_1718(roster_data_1718):
    roster_1718 = api_teams_roster_id.search(roster_data_1718)
    return roster_1718

#Finding players that are part of the team in both seasons
def players_in_both(roster_1617, roster_1718):
    players_in_both, found_players = tf.find_players(roster_1617, roster_1718)
    return players_in_both, found_players

# For TEST2
# Reusing players_in_both to collect the points information from people function
def roster_1617_points(url_people,players_in_both,url_stats_1617,api_points):
    roster_1617_points, empty_value_1617, collect_1617, response_state_1617 = tf.create_list_multiple(url_people,players_in_both,url_stats_1617,api_points)
    return roster_1617_points, empty_value_1617, collect_1617, response_state_1617

def roster_1718_points(url_people,players_in_both,url_stats_1718,api_points):
    roster_1718_points, empty_value_1718, collect_1718, response_state_1718 = tf.create_list_multiple(url_people,players_in_both,url_stats_1718,api_points)
    return roster_1718_points, empty_value_1718, collect_1718, response_state_1718

# Calculate team points
def team_points_1617(roster_1617_points):
    team_points_1617, calculate_1617 = tf.calculate_team_points(roster_1617_points)
    return team_points_1617, calculate_1617

def team_points_1718(roster_1718_points):
    team_points_1718, calculate_1718 = tf.calculate_team_points(roster_1718_points)
    return team_points_1718, calculate_1718
# For TEST3
# Using roster_1718 to find if there is a difference between teams and people functions
# Getting the teams using teams functions

# Creates a list based in the team
def people_current_team(url_people,roster_1718,key,api_people_currentTeam):
    people_current_team, t3_empty_value_current, t3_collect_current, t3_response_state_current  = tf.create_list_multiple(url_people,roster_1718,key,api_people_currentTeam)
    return people_current_team, t3_empty_value_current, t3_collect_current, t3_response_state_current

# Create a list with the player position using the teams function
#def teams_position(roster_data_1718):
#    teams_position = api_teams_position.search(roster_data_1718)

# Create a list with the player position using the people function
def people_position(url_people,roster_1718,key,api_people_position):
    people_position, t3_empty_value_position, t3_collect_position, t3_response_state_position = tf.create_list_multiple(url_people,roster_1718,key,api_people_position)
    return people_position, t3_empty_value_position, t3_collect_position, t3_response_state_position
