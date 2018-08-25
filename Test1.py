import test_functions as tf
import test_procedures as tp

config = tf.load_config('config.json')

min_num_players = config['TEST1']['MIN_NUMBER_PLAYERS']

if len(tp.players_in_both) >= min_num_players:
    print('TEST PASS '  + str(len(tp.players_in_both)) + ' players were in both seasons')
else:
    print('TEST FAIL')
