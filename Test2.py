import test_functions as tf
import test_procedures as tp

improve_count = 0
noImprove_count = 0
counter = len(tp.roster_1617_points) - 1

print('Executing TEST CASE 2')

if tp.t2_response_state_1617 and tp.t2_response_state_1718 == True:
    print('Sending and receiving data')
else:
    if tp.t2_response_state_1617 == False:
        print('There is a problem with the 2016-2017 request')
    else:
        print('There is a problem with the 2017-2018 request')
if tp.t2_collect_1617 and tp.t2_collect_1718 == True:
    print('Collecting players points')
else:
    if tp.t2_collect_1617 == False:
        print('There is a problem collecting 2016-2017 data')
    else:
        print('There is a problem collecting 2017-2018 data')
if tp.t2_empty_value_1617 or tp.t2_empty_value_1718 == True:
    print('WARNING: there are some empty values in the API, maybe a bug?, replaced with N/A')
if tp.t2_calculate_1617 and tp.t2_calculate_1718 == True:
    print('Calculating points')
else:
    if tp.t2_calculate_1617 == False:
        print('There is a problem calculating 2016-2017 points')
    else:
        print('There is a problem calculating 2017-2018 points')

# Test2a Have all the players in the 2016-2017 and 2017-2018 roster improved?

print('Validating TEST 2A')

while counter >= 0:
    if type(tp.roster_1617_points[counter]) and type(tp.roster_1718_points[counter])  == int: #Some goalies have no points
        if tp.roster_1617_points[counter] < tp.roster_1718_points[counter]:
            improve_count = improve_count + 1
        else:
            noImprove_count = noImprove_count + 1
    counter = counter - 1

if noImprove_count > 0:
    print(tp.separator)
    print('Test 2A FAIL: Only ' + str(noImprove_count) + ' players had more points in season 2016-2017')
    print(tp.separator)
else:
    print(tp.separator)
    print('Test 2A PASS: All players improved')
    print(tp.separator)

#Test2b Has the team improved?

print('Validating TEST 2B')

if tp.team_points_1617 < tp.team_points_1718:
    print(tp.separator)
    print('Test 2B PASS: The team improved from last season, more points in season 2017-2018')
    print(tp.separator)
else:
    print(tp.separator)
    print('Test 2B FAIL: The team did not improve, more points in season 2016-2017')
    print(tp.separator)
