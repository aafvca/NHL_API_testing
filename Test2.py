import test_functions as tf
import test_procedures as tp
import messages as mg
import jmespath

config = tf.load_config('config.json')

url_teams = config['DEFAULT']['TEAMS_URL']
url_people = config['DEFAULT']['PEOPLE_URL']
url_stats_1617 = config['TEST2']['MTL_STATS_1617']
url_stats_1718 = config['TEST2']['MTL_STATS_1718']
url_team_1617 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1617']
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
api_teams_roster_id = jmespath.compile(config['TEST1']['API_TEAMS_ROSTER_ID'])
api_points =jmespath.compile(config['TEST2']['API_POINTS'])
improve_count = 0
noImprove_count = 0
season_1617 = '2016-2017'
season_1718 = '2017-2018'
TC2A_label = 'Test_Case_2A'
TC2B_label = 'Test_Case_2B'

print('Executing ' + TC2A_label)

roster_data_1617, t2_response_state_1617 = tp.roster_data_1617(url_team_1617)
roster_data_1718, t2_response_state_1718 = tp.roster_data_1718(url_team_1718)

tf.response_state(t2_response_state_1617, t2_response_state_1718, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, season_1617, season_1718)

print('Collecting player IDs')
roster_1617 = tp.roster_1617(roster_data_1617)
roster_1718 = tp.roster_1718(roster_data_1718)

print('Finding players in both seasons')
players_in_both, t2_found_players = tp.players_in_both(roster_1617,roster_1718)

print('Collecting players points')
roster_1617_points, t2_empty_value_1617, t2_collect_1617, t2_response_state_1617 = tp.roster_1617_points(url_people,players_in_both,url_stats_1617,api_points)
roster_1718_points, t2_empty_value_1718, t2_collect_1718, t2_response_state_1718 = tp.roster_1718_points(url_people,players_in_both,url_stats_1718,api_points)

tf.response_state(t2_collect_1617, t2_collect_1718, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, season_1617, season_1718)

tf.empty_value(t2_empty_value_1617, t2_empty_value_1718)

team_points_1617, t2_calculate_1617 = tp.team_points_1617(roster_1617_points)
team_points_1718, t2_calculate_1718 = tp.team_points_1617(roster_1718_points)

tf.response_state(t2_calculate_1617, t2_calculate_1718, mg.calculate_ok, mg.calculate_nok_preffix, mg.calculate_nok_suffix, season_1617, season_1718)

# Test2a Have all the players in the 2016-2017 and 2017-2018 roster improved?

print('Validating ' + TC2A_label)

log_info = {'roster points 1716': roster_1617_points, 'roster points 1718': roster_1718_points, 'team points 1617': team_points_1617, 'team points 1718': team_points_1718}

counter = len(roster_1617_points) - 1

while counter >= 0:
    if type(roster_1617_points[counter]) and type(roster_1718_points[counter])  == int: #Some goalies have no points
        if roster_1617_points[counter] < roster_1718_points[counter]:
            improve_count = improve_count + 1
        else:
            noImprove_count = noImprove_count + 1
    counter = counter - 1

if noImprove_count > 0:
    tf.test_fail(TC2A_label, str(noImprove_count) + mg.t2a_fail)
    tf.log_creation(TC2A_label,log_info)
else:
    tf.test_pass(TC2A_label, mg.t2a_pass)
    #tf.log_creation(TC1_label,log_info)

#Test2b Has the team improved?

print('Validating ' + TC2B_label)

if team_points_1617 < team_points_1718:
    tf.test_pass(TC2B_label, mg.t2b_pass)
    #tf.log_creation(TC1_label,log_info)
else:
    tf.test_fail(TC2B_label, mg.t2b_fail)
    tf.log_creation(TC2B_label,log_info)
