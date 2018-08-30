import sys
import test_functions as tf
import test_procedures as tp
import messages as mg
import jmespath

config = tf.load_config('config.json')
suite = config['DEFAULT']['SUITE']

url_people = config['DEFAULT']['PEOPLE_URL']
api_people_currentTeam = jmespath.compile(config['TEST3']['API_PEOPLE_CURRENT_TEAM'])
api_teams_position = jmespath.compile(config['TEST3']['API_TEAMS_POSITION'])
api_people_position = jmespath.compile(config['TEST3']['API_PEOPLE_POSITION'])
url_team_1718 = config['DEFAULT']['TEAMS_URL'] + config['TEST1']['MTL_ROSTER_1718']
TC3A_label = config['TEST3']['TC3A_LABEL']
TC3B_label = config['TEST3']['TC3B_LABEL']
t_pass = config['DEFAULT']['TEST PASS']
t_fail = config['DEFAULT']['TEST FAIL']
t_noexec = config['TEST3']['TEST NOT EXECUTED']
not_canadien = 0
not_same_team = 0

if sys.argv[0] == "Test_Suite.py":
    suite = 'True'

# Test 3a: Validate if currentTeam returned by people function is Montreal Canadiens

print('Executing TC3')

# Collect roster information from season 2017-2018
roster_data_1718, t3_response_state_1718 = tp.roster_data(url_team_1718)

tf.response_state(t3_response_state_1718, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, mg.tc31_msg_label)

# Using the roster information obtain the playerIDs for further processing
print('Collecting player IDs')
roster_1718 = tp.roster_list(roster_data_1718)

# Obtain the current team info using the people function
print('Collecting info from people currentTeam')

people_current_team, t3_empty_value_current, t3_collect_current, t3_response_state_current  = tp.people_current_team(url_people,roster_1718,'/',api_people_currentTeam)

tf.response_state(t3_collect_current, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, mg.tc31_msg_label)

# Locate empty values and replace with 'N/A'
print('Looking for empty values')
tf.empty_value(t3_empty_value_current)

# Test 3b
# Are positions returned by teams are the same as people?

# Obtain the position info using the teams function
print('Finding position using teams function')
teams_position = api_teams_position.search(roster_data_1718)

people_position, t3_empty_value_position, t3_collect_position, t3_response_state_position = tp.people_position(url_people,roster_1718,'/',api_people_position)

tf.response_state(t3_response_state_position, mg.response_ok, mg.response_nok_preffix, mg.response_nok_suffix, mg.tc32_msg_label)

# Obtain the position info using the people function
print('Finding position using people function')
tf.response_state(t3_collect_position, mg.collect_ok, mg.collect_nok_preffix, mg.collect_nok_suffix, mg.tc32_msg_label)

# Locate empty values and replace with 'N/A'
print('Looking for empty values')
tf.empty_value(t3_empty_value_position)

print('Validating ' + TC3A_label)

#Log and Test Case validation info
log_info1 = {'currentTeam from people': people_current_team }

# TC3A: CurrentTeam returned by people function should be Montréal Canadiens"
for player in people_current_team:
    if 'Montréal Canadiens' not in player:
        not_canadien = not_canadien + 1

if not_canadien != 0:
    tf.test_fail(TC3A_label, mg.t3a_fail)
    tf.log_creation(TC3A_label,log_info1)
    t_fail = t_fail + 1
    t_noexec = t_noexec - 1
else:
    tf.test_pass(TC3A_label, mg.t3b_pass)
    #tf.log_creation(TC3A_label,log_info)
    t_pass = t_pass + 1
    t_noexec = t_noexec - 1

print('Validating ' + TC3B_label)

#Log and Test Case validation info
log_info2 = {'positions from team': teams_position, 'positions from people': people_position }


# TC3B: The players position returned by people function and teams function should be the same
counter = len(teams_position) - 1

while counter >= 0:
    if teams_position[counter] != people_position[counter]:
        not_same_team = not_same_team + 1
    counter = counter - 1

if not_same_team == 0:
    tf.test_pass(TC3B_label, mg.t3b_pass)
    #tf.log_creation(TC3B_label,log_info)
    t_pass = t_pass + 1
    t_noexec = t_noexec - 1
else:
    tf.test_fail(TC3B_label, mg.t3b_fail)
    tf.log_creation(TC3B_label,log_info2)
    t_fail = t_fail + 1
    t_noexec = t_noexec - 1

# Test summary will be executed if the TC is executed individually
if suite == 'False':
    tf.test_summary(t_pass,t_fail,t_noexec)
