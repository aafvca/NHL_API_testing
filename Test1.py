import test_functions as tf
import test_procedures as tp

config = tf.load_config('config.json')

min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']

print('Executing TEST CASE 1')

if tp.t1_response_state_1617 and tp.t1_response_state_1718 == True:
    print('Sending and receiving data')
else:
    if tp.t1_response_state_1617 == False:
        print('There is a problem with the 2016-2017 request')
    else:
        print('There is a problem with the 2017-2018 request')

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
