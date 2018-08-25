import test_functions as tf
import json, jmespath
from urllib.request import urlopen

config = tf.load_config('config.json')
#with open('config.json', 'r') as f:
    #config = json.load(f)

url_teams = config['DEFAULT']['TEAMS_URL']
url_people = config['DEFAULT']['PEOPLE_URL']
url_stats1617 = config['TEST2']['MTL_STATS_1617']
url_stats1718 = config['TEST2']['MTL_STATS_1718']
url_team_1617 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1617']
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
api_roster_id = jmespath.compile(config['TEST1']['API_ROSTER_ID'])

# For TEST1
# Get the API response for both rosters 2016-2017 and 2017-2018
print('Collecting roster information for 2016-2017 team')
roster_data_1617 = tf.get_response(url_team_1617)
print('Collecting roster information for 2017-2018 team')
roster_data_1718 = tf.get_response(url_team_1718)

roster_1617 = api_roster_id.search(roster_data_1617)
roster_1718 = api_roster_id.search(roster_data_1718)

#Finding players that are part of the team in both seasons
print('Finding players')
players_in_both = tf.find_players(roster_1617, roster_1718)
