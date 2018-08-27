import test_functions as tf
import test_procedures as tp
import messages as mg

config = tf.load_config('config.json')

url_teams = config['DEFAULT']['TEAMS_URL']
url_people = config['DEFAULT']['PEOPLE_URL']
url_stats_1617 = config['TEST2']['MTL_STATS_1617']
url_stats_1718 = config['TEST2']['MTL_STATS_1718']
url_team_1617 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1617']
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']
season_1617 = '2016-2017'
season_1718 = '2017-2018'
TC1_label = 'Test_Case_1'

print('Executing ' + TC1_label)

roster_data_1617, t1_response_state_1617 = tp.roster_data_1617(url_team_1617)
roster_data_1718, t1_response_state_1718 = tp.roster_data_1718(url_team_1718)

tf.response_state(t1_response_state_1617, t1_response_state_1718, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, season_1617, season_1718)

print('Collecting player IDs')
roster_1617 = tp.roster_1617(roster_data_1617)
roster_1718 = tp.roster_1718(roster_data_1718)

print('Finding players in both seasons')
players_in_both, t1_found_players = tp.players_in_both(roster_1617,roster_1718)

log_info = {'roster 2016-2017': roster_1617, 'roster 2017-2018': roster_1718, 'players in both seasons' : players_in_both}
tpass_msg = str(len(players_in_both)) + ' players were in both seasons'
tfail_msg = 'Less than 10 players ere in both seasons'

if t1_found_players == True:
    print("Searching for players in both rosters")

print('Validating ' + TC1_label)

#Log and Test Case validation info
log_info = log_info = {'roster 2016-2017': roster_1617, 'roster 2017-2018': roster_1718, 'players in both seasons' : players_in_both}
tpass_msg = str(len(players_in_both)) + ' players were in both seasons'
tfail_msg = 'Less than 10 players ere in both seasons'

if len(players_in_both) >= min_num_players:
    tf.test_pass(TC1_label, str(len(players_in_both)) + mg.tc1_pass)
    #tf.log_creation(TC1_label,log_info)
else:
    tf.test_fail(TC1_label, mg.tc1_fail)
    tf.log_creation(TC1_label,log_info)
