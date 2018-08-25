import test_functions as tf
import test_procedures as tp

improve_count = 0
noImprove_count = 0
counter = len(tp.roster_1617_points) - 1


# Test2a Have all the players in the 2016-2017 and 2017-2018 roster improved?

print('Validate Test 2a')

while counter >= 0:
    if type(tp.roster_1617_points[counter]) and type(tp.roster_1718_points[counter])  == int: #Some goalies have no points
        if tp.roster_1617_points[counter] < tp.roster_1718_points[counter]:
            improve_count = improve_count + 1
        else:
            noImprove_count = noImprove_count + 1
    counter = counter - 1

if noImprove_count > 0:
    print('Test1 Failed ' + str(noImprove_count) + ' players did not improve')
else:
    print('Test1 Passed all players improved')

#Test2b Has the team improved?

print('Validate Test 2b')

if tp.team_points_1617 < tp.team_points_1718:
    print('Test 2 Passed: The team improved from last season')
else:
    print('Test 2 Failed: The team did not improve')
