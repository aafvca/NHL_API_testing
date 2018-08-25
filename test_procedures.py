import test_functions as tf
import json, jmespath
from urllib.request import urlopen

config = tf.load_config('config.json')
#with open('config.json', 'r') as f:
    #config = json.load(f)

url_teams = config['DEFAULT']['TEAMS_URL']
url_people = config['DEFAULT']['PEOPLE_URL']
url_stats_1617 = config['TEST2']['MTL_STATS_1617']
url_stats_1718 = config['TEST2']['MTL_STATS_1718']
url_team_1617 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1617']
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
api_teams_roster_id = jmespath.compile(config['TEST1']['API_TEAMS_ROSTER_ID'])
api_points =jmespath.compile(config['TEST2']['API_POINTS'])
api_people_currentTeam = jmespath.compile(config['TEST3']['API_PEOPLE_CURRENT_TEAM'])
api_teams_position = jmespath.compile(config['TEST3']['API_TEAMS_POSITION'])
api_people_position = jmespath.compile(config['TEST3']['API_PEOPLE_POSITION'])

# For TEST1
# Get the API response for both rosters 2016-2017 and 2017-2018
print('Collecting roster information for 2016-2017 team')
roster_data_1617 = tf.get_response(url_team_1617)
print('Collecting roster information for 2017-2018 team')
roster_data_1718 = tf.get_response(url_team_1718)

# Creates a list based in roster id
roster_1617 = api_teams_roster_id.search(roster_data_1617)
roster_1718 = api_teams_roster_id.search(roster_data_1718)

#Finding players that are part of the team in both seasons
print('Finding players')
players_in_both = tf.find_players(roster_1617, roster_1718)

# For TEST2
# Reusing players_in_both to collect the points information from people function
nested_roster_1617_points = tf.create_list_multiple(url_people,players_in_both,url_stats_1617,api_points)
nested_roster_1718_points = tf.create_list_multiple(url_people,players_in_both,url_stats_1718,api_points)

# Create singles list from nested
roster_1617_points = tf.single_from_nested(nested_roster_1617_points)
roster_1718_points = tf.single_from_nested(nested_roster_1718_points)

# Calculate team points
team_points_1617 = tf.calculate_team_points(roster_1617_points)
team_points_1718 = tf.calculate_team_points(roster_1718_points)

# For TEST3
# Using roster_1718 to find if there is a difference between teams and people functions
# Getting the teams using teams functions

# Creates a list based in the team
nested_current_team = tf.create_list_multiple(url_people,roster_1718,'/',api_people_currentTeam)

# Create a single list from nested
people_current_team = tf.single_from_nested(nested_current_team)
