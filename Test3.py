import test_functions as tf
import test_procedures as tp

# Validate if currentTeam returned by people function is Montreal Canadiens
not_canadien = 0

for player in tp.people_current_team:
    if 'Montréal Canadiens' not in player:
        not_canadien = not_canadien + 1

if not_canadien != 0:
    print('Test 3a Failed, some players have different or no team')
else:
    print('Test 3a Passed, all players have Montréal Canadiens as team')
