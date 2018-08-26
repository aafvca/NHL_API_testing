import test_functions as tf
import test_procedures as tp

not_canadien = 0
not_same_team = 0

# Test 3a: Validate if currentTeam returned by people function is Montreal Canadiens

for player in tp.people_current_team:
    if 'Montréal Canadiens' not in player:
        not_canadien = not_canadien + 1

if not_canadien != 0:
    print('Test 3a Failed, some players have different or no team')
else:
    print('Test 3a Passed, all players have Montréal Canadiens as team')

# Test 3b
# Are positions returned by teams are the same as people?

counter = len(tp.teams_position) - 1

while counter >= 0:
    if tp.teams_position[counter] != tp.people_position[counter]:
        not_same_team = not_same_team + 1
    counter = counter - 1

if not_same_team == 0:
    print('Test3b Passed: Both functions showed the same position')
else:
    print('Test3b Failed: There are differences between the two functions')
