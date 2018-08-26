import test_functions as tf
import test_procedures as tp
import messages as mg

config = tf.load_config('config.json')

min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']
season_1617 = '2016-2017'
season_1718 = '2017-2018'

print('Executing TEST CASE 1')

if tp.t1_response_state_1617 and tp.t1_response_state_1718 == True:
    print(mg.response_ok)
else:
    if tp.t1_response_state_1617 == False:
        print(mg.response_nok_preffix + season_1617  + mg.response_nok_suffix)
    else:
        print(mg.response_nok_preffix + season_1718  + mg.response_nok_suffix)

if tp.t1_found_players == True:
    print("Searching for players in both rosters")

print('Validating TEST 1')

if len(tp.players_in_both) >= min_num_players:
    print(tp.separator)
    print('TEST 1 PASS: '  + str(len(tp.players_in_both)) + ' players were in both seasons')
    print(tp.separator)
else:
    print(tp.separator)
    print('TEST 1 FAIL: Less than 10 players ere in both seasons')
    print(tp.separator)
