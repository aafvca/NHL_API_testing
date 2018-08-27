import sys
import test_functions as tf
import test_procedures as tp
import messages as mg
import jmespath

config = tf.load_config('config.json')

suite = config['DEFAULT']['SUITE']
url_teams = config['DEFAULT']['TEAMS_URL']
url_people = config['DEFAULT']['PEOPLE_URL']
url_stats_1617 = config['TEST2']['MTL_STATS_1617']
url_stats_1718 = config['TEST2']['MTL_STATS_1718']
url_team_1617 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1617']
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
api_teams_roster_id = jmespath.compile(config['TEST1']['API_TEAMS_ROSTER_ID'])
api_points =jmespath.compile(config['TEST2']['API_POINTS'])
season_1617 = config['DEFAULT']['SEASON 2016-2017']
season_1718 = config['DEFAULT']['SEASON 2016-2017']
TC2A_label = config['TEST2']['TC2A_LABEL']
TC2B_label = config['TEST2']['TC2B_LABEL']
t_pass = config['DEFAULT']['TEST PASS']
t_fail = config['DEFAULT']['TEST FAIL']
t_noexec = config['TEST2']['TEST NOT EXECUTED']
improve_count = 0
noImprove_count = 0

# Find out if this is a suite execution
if sys.argv[0] == "Test_Suite.py":
    suite = 'True'

print('Executing TC2')

# Collect roster information from seasons 2016-2017 and 2017-2018
roster_data_1617, t2_response_state_1617 = tp.roster_data_1617(url_team_1617)
roster_data_1718, t2_response_state_1718 = tp.roster_data_1718(url_team_1718)

tf.response_state(t2_response_state_1617, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, season_1617)
tf.response_state(t2_response_state_1718, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, season_1718)

# Using the roster information obtain the playerIDs for further processing
print('Collecting player IDs')
roster_1617 = tp.roster_1617(roster_data_1617)
roster_1718 = tp.roster_1718(roster_data_1718)

# Look in both lists for matches
print('Finding players in both seasons')
players_in_both, t2_found_players = tp.players_in_both(roster_1617,roster_1718)

# Obtain the points information for season 2016-2017 and 2017-2018
print('Collecting players points')
roster_1617_points, t2_empty_value_1617, t2_collect_1617, t2_response_state_1617 = tp.roster_1617_points(url_people,players_in_both,url_stats_1617,api_points)
roster_1718_points, t2_empty_value_1718, t2_collect_1718, t2_response_state_1718 = tp.roster_1718_points(url_people,players_in_both,url_stats_1718,api_points)

tf.response_state(t2_collect_1617, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, season_1617)
tf.response_state(t2_collect_1718, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, season_1718)

# Locate empty values and replace with 'N/A'
tf.empty_value(t2_empty_value_1617)
tf.empty_value(t2_empty_value_1718)

# Calculate the team points for both seasons
team_points_1617, t2_calculate_1617 = tp.team_points_1617(roster_1617_points)
team_points_1718, t2_calculate_1718 = tp.team_points_1617(roster_1718_points)

tf.response_state(t2_calculate_1617, mg.calculate_ok, mg.calculate_nok_preffix, mg.calculate_nok_suffix, season_1617)
tf.response_state(t2_calculate_1718, mg.calculate_ok, mg.calculate_nok_preffix, mg.calculate_nok_suffix, season_1718)

# Test2a Have all the players in the 2016-2017 and 2017-2018 roster improved? Yes if they have more points in 2017-2018 season

print('Validating ' + TC2A_label)

#Log and Test Case validation info
log_info = {'roster points 1716': roster_1617_points, 'roster points 1718': roster_1718_points, 'team points 1617': team_points_1617, 'team points 1718': team_points_1718}

counter = len(roster_1617_points) - 1

while counter >= 0:
    if type(roster_1617_points[counter]) and type(roster_1718_points[counter])  == int:
        if roster_1617_points[counter] < roster_1718_points[counter]:
            improve_count = improve_count + 1
        else:
            noImprove_count = noImprove_count + 1
    counter = counter - 1

if noImprove_count > 0:
    tf.test_fail(TC2A_label, str(noImprove_count) + mg.t2a_fail)
    tf.log_creation(TC2A_label,log_info)
    t_fail = t_fail + 1
    t_noexec = t_noexec - 1
else:
    tf.test_pass(TC2A_label, mg.t2a_pass)
    t_pass = t_pass + 1
    t_noexec = t_noexec - 1
    #tf.log_creation(TC1_label,log_info)

#Test2b Has the overall team improved? Yes if the team has more points in 2017-2018 season

print('Validating ' + TC2B_label)

if team_points_1617 < team_points_1718:
    tf.test_pass(TC2B_label, mg.t2b_pass)
    t_pass = t_pass + 1
    t_noexec = t_noexec - 1
    #tf.log_creation(TC1_label,log_info)
else:
    tf.test_fail(TC2B_label, mg.t2b_fail)
    tf.log_creation(TC2B_label,log_info)
    t_fail = t_fail + 1
    t_noexec = t_noexec - 1

# Test summary will be executed if the TC is executed individually	
if suite == 'False':
    tf.test_summary(t_pass,t_fail,t_noexec)
