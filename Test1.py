import test_functions as tf
import test_procedures as tp
import messages as mg

config = tf.load_config('config.json')

log_info = {'roster 2016-2017': tp.roster_1617, 'roster 2017-2018': tp.roster_1718, 'players in both seasons' : tp.players_in_both}
min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']
tpass_msg = str(len(tp.players_in_both)) + ' players were in both seasons'
tfail_msg = 'Less than 10 players ere in both seasons'
season_1617 = '2016-2017'
season_1718 = '2017-2018'
TC1_label = 'Test_Case_1'

print('Executing ' + TC1_label)

if tp.t1_response_state_1617 and tp.t1_response_state_1718 == True:
    print(mg.response_ok)
else:
    if tp.t1_response_state_1617 == False:
        print(mg.response_nok_preffix + season_1617  + mg.response_nok_suffix)
    else:
        print(mg.response_nok_preffix + season_1718  + mg.response_nok_suffix)

if tp.t1_found_players == True:
    print("Searching for players in both rosters")

print('Validating ' + TC1_label)

if len(tp.players_in_both) >= min_num_players:
    tf.test_pass(TC1_label, tpass_msg)
    #tf.log_creation(TC1_label,log_info)
else:
    tf.test_fail(TC1_label, tfail_msg)
    tf.log_creation(TC1_label,log_info)
