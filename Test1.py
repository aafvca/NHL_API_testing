import sys
import test_functions as tf
import test_procedures as tp
import messages as mg

config = tf.load_config('config.json')

suite = config['DEFAULT']['SUITE']
url_teams = config['DEFAULT']['TEAMS_URL']
url_people = config['DEFAULT']['PEOPLE_URL']
url_team_1617 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1617']
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']
season_1617 = config['DEFAULT']['SEASON 2016-2017']
season_1718 = config['DEFAULT']['SEASON 2016-2017']
TC1_label = config['TEST1']['TC1_label']
t_pass = config['DEFAULT']['TEST PASS']
t_fail = config['DEFAULT']['TEST FAIL']

# Find out if this is a suite execution
if sys.argv[0] == "Test_Suite.py":
    suite = 'True'

print('Executing ' + TC1_label)

# Collect roster information from seasons 2016-2017 and 2017-2018
roster_data_1617, status_code = tp.roster_data(url_team_1617)
roster_data_1718, status_code = tp.roster_data(url_team_1718)

# Validatating status_code = 200 OK
if status_code != 200:
    print('There is a problem with the GET response code')

# Using the roster information obtain the playerIDs for further processing
print('Collecting player IDs')
roster_1617 = tp.roster_list(roster_data_1617)
roster_1718 = tp.roster_list(roster_data_1718)

# Look in both lists for matches
print('Finding players in both seasons')
players_in_both = tp.players_in_both(roster_1617,roster_1718)

print('Validating ' + TC1_label)

#Log and Test Case validation info
log_info = {'roster 2016-2017': roster_1617, 'roster 2017-2018': roster_1718, 'players in both seasons' : players_in_both}

# If at least 10 players are in both seasons the TC will pass
if len(players_in_both) >= min_num_players:
    tf.test_pass(TC1_label, str(len(players_in_both)) + mg.tc1_pass)
    #tf.log_creation(TC1_label,log_info)
    t_pass = t_pass + 1
else:
    tf.test_fail(TC1_label, mg.tc1_fail)
    tf.log_creation(TC1_label,log_info)
    t_fail = t_fail + 1

# Test summary will be executed if the TC is executed individually
if suite == 'False':
    tf.test_summary(t_pass,t_fail,t_noexec)
