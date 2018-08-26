import test_functions as tf
import test_procedures as tp

not_canadien = 0
not_same_team = 0

# Test 3a: Validate if currentTeam returned by people function is Montreal Canadiens

print('Executing TEST CASE 3')

if tp.t3_response_state_current == True:
    print('Sending and receiving data')
else:
    print('There is a problem with the currentTeam request')
if tp.t3_collect_current == True:
    print('Collecting players team')
else:
    print('There is a problem collecting team data')
if tp.t3_empty_value_current == True:
    print('WARNING: there are some empty values in the API, maybe a bug?, replaced with N/A')

print('Validating TEST 3A')

for player in tp.people_current_team:
    if 'Montréal Canadiens' not in player:
        not_canadien = not_canadien + 1

if not_canadien != 0:
    print(tp.separator)
    print('Test 3A FAIL: Some players have different or no team in people currentTeam')
    print(tp.separator)
else:
    print(tp.separator)
    print('Test 3A PASS: All players have Montréal Canadiens as team')
    print(tp.separator)

# Test 3b
# Are positions returned by teams are the same as people?

if tp.t3_response_state_position == True:
    print('Sending and receiving data')
else:
    print('There is a problem with the position request')
if tp.t3_collect_position == True:
    print('Collecting players team')
else:
    print('There is a problem collecting position data')
if tp.t3_empty_value_position == True:
    print('WARNING: there are some empty values in the API, maybe a bug?')

print('Validating TEST 3B')

counter = len(tp.teams_position) - 1

while counter >= 0:
    if tp.teams_position[counter] != tp.people_position[counter]:
        not_same_team = not_same_team + 1
    counter = counter - 1

if not_same_team == 0:
    print(tp.separator)
    print('Test 3B PASS: Both functions showed the same position for every player')
    print(tp.separator)
else:
    print(tp.separator)
    print('Test 3B FAIL: There are differences in positions between the two functions')
    print(tp.separator)
