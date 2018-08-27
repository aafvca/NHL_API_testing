import test_functions as tf
import test_procedures as tp
import messages as mg
import jmespath

config = tf.load_config('config.json')

#log_info = {'currentTeam from people': people_current_team, 'positions from team': teams_position, 'positions from people': people_position }
not_canadien = 0
not_same_team = 0
url_people = config['DEFAULT']['PEOPLE_URL']
api_people_currentTeam = jmespath.compile(config['TEST3']['API_PEOPLE_CURRENT_TEAM'])
api_teams_position = jmespath.compile(config['TEST3']['API_TEAMS_POSITION'])
api_people_position = jmespath.compile(config['TEST3']['API_PEOPLE_POSITION'])
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
tc1_msg_label = 'currentTeam'
tc2_msg_label = 'position'
TC3A_label = 'Test_Case_3A'
t3a_pass_msg = 'All players have Montréal Canadiens as team'
t3a_fail_msg = 'Some players have different or no team in people currentTeam'
TC3B_label = 'Test_Case_3B'
t3b_pass_msg = 'Both functions showed the same position for every player'
t3b_fail_msg = 'There are differences in positions between the two functions'

# Test 3a: Validate if currentTeam returned by people function is Montreal Canadiens

print('Executing ' + TC3A_label)

roster_data_1718, t3_response_state_1718 = tp.roster_data_1718(url_team_1718)

tf.response_state_single(t3_response_state_1718, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, tc1_msg_label)

print('Collecting player IDs')
roster_1718 = tp.roster_1718(roster_data_1718)
print(roster_1718)

print('Collecting info from people currentTeam')

people_current_team, t3_empty_value_current, t3_collect_current, t3_response_state_current  = tp.people_current_team(url_people,roster_1718,'/',api_people_currentTeam)

tf.response_state_single(t3_collect_current, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, tc1_msg_label)

print('Looking for empty values')
tf.empty_value_single(t3_empty_value_current)

print('Validating ' + TC3A_label)

for player in people_current_team:
    if 'Montréal Canadiens' not in player:
        not_canadien = not_canadien + 1

if not_canadien != 0:
    tf.test_fail(TC3A_label, t3a_fail_msg)
    tf.log_creation(TC3A_label,log_info)
else:
    tf.test_pass(TC3A_label, t3b_pass_msg)
    #tf.log_creation(TC3A_label,log_info)

# Test 3b
# Are positions returned by teams are the same as people?
print('Executing ' + TC3B_label)

print('Finding position using teams function')
teams_position = api_teams_position.search(roster_data_1718)

people_position, t3_empty_value_position, t3_collect_position, t3_response_state_position = tp.people_position(url_people,roster_1718,'/',api_people_position)

tf.response_state_single(t3_response_state_position, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, tc2_msg_label)

print('Finding position using people function')
tf.response_state_single(t3_collect_position, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, tc2_msg_label)

print('Looking for empty values')
tf.empty_value_single(t3_empty_value_position)

print('Validating ' + TC3B_label)

counter = len(teams_position) - 1

while counter >= 0:
    if teams_position[counter] != people_position[counter]:
        not_same_team = not_same_team + 1
    counter = counter - 1

if not_same_team == 0:
    tf.test_pass(TC3B_label, t3b_pass_msg)
    #tf.log_creation(TC3B_label,log_info)
else:
    tf.test_fail(TC3B_label, t3b_fail_msg)
    tf.log_creation(TC3B_label,log_info)
