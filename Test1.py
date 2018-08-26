import test_functions as tf
import test_procedures as tp
import messages as mg

config = tf.load_config('config.json')

min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']
season_1617 = '2016-2017'
season_1718 = '2017-2018'
TC1_label = 'Test_Case_1'

print('Executing ' + TC1_label)

roster_data_1617, t1_response_state_1617 = tp.roster_data_1617()
roster_data_1718, t1_response_state_1718 = tp.roster_data_1718()

tf.response_state(t1_response_state_1617, t1_response_state_1718, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, season_1617, season_1718)

roster_1617 = tp.roster_1617(roster_data_1617)
roster_1718 = tp.roster_1718(roster_data_1718)

players_in_both, t1_found_players = tp.players_in_both(roster_1617,roster_1718)

log_info = {'roster 2016-2017': roster_1617, 'roster 2017-2018': roster_1718, 'players in both seasons' : players_in_both}
tpass_msg = str(len(players_in_both)) + ' players were in both seasons'
tfail_msg = 'Less than 10 players ere in both seasons'

if t1_found_players == True:
    print("Searching for players in both rosters")

print('Validating ' + TC1_label)

#Log and Test Case validation info
log_info = {'roster 2016-2017': roster_1617, 'roster 2017-2018': roster_1718, 'players in both seasons' : players_in_both}
tpass_msg = str(len(players_in_both)) + ' players were in both seasons'
tfail_msg = 'Less than 10 players ere in both seasons'

if len(players_in_both) >= min_num_players:
    tf.test_pass(TC1_label, tpass_msg)
    #tf.log_creation(TC1_label,log_info)
else:
    tf.test_fail(TC1_label, tfail_msg)
    tf.log_creation(TC1_label,log_info)
