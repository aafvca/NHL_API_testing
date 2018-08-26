import test_functions as tf
import test_procedures as tp
import messages as mg


not_canadien = 0
not_same_team = 0
tc1_msg_label = 'currentTeam'
tc2_msg_label = 'position'
TC3A_label = 'TEST CASE 3A'
t3a_pass_msg = 'All players have Montréal Canadiens as team'
t3a_fail_msg = 'Some players have different or no team in people currentTeam'
TC3B_label = 'TEST CASE 3B'
t3b_pass_msg = 'Both functions showed the same position for every player'
t3b_fail_msg = 'There are differences in positions between the two functions'

# Test 3a: Validate if currentTeam returned by people function is Montreal Canadiens

print('Executing ' + TC3A_label)

if tp.t3_response_state_current == True:
    print(mg.response_ok)
else:
    print(mg.response_nok_suffix + tc1_msg_label  + mg.response_nok_preffix)

if tp.t3_collect_current == True:
    print(mg.collect_ok)
else:
    print(mg.collect_nok_preffix + tc1_msg_label + mg.collect_nok_suffix)

if tp.t3_empty_value_current == True:
    print(mg.empty_value)

print('Validating ' + TC3A_label)

for player in tp.people_current_team:
    if 'Montréal Canadiens' not in player:
        not_canadien = not_canadien + 1

if not_canadien != 0:
    tf.test_pass(TC3A_label, t3a_fail_msg)
else:
    tf.test_pass(TC3A_label, t3b_pass_msg)

# Test 3b
# Are positions returned by teams are the same as people?

if tp.t3_response_state_position == True:
    print(mg.response_ok)
else:
    print(mg.response_nok_suffix + tc2_msg_label  + mg.response_nok_preffix)

if tp.t3_collect_position == True:
    print(mg.collect_ok)
else:
    print(mg.collect_nok_preffix + tc2_msg_label + mg.collect_nok_suffix)

if tp.t3_empty_value_position == True:
    print(mg.empty_value)

print('Validating TEST 3B')

counter = len(tp.teams_position) - 1

while counter >= 0:
    if tp.teams_position[counter] != tp.people_position[counter]:
        not_same_team = not_same_team + 1
    counter = counter - 1

if not_same_team == 0:
    tf.test_pass(TC3B_label, t3b_pass_msg)
else:
    tf.test_pass(TC3B_label, t3b_pass_msg)
