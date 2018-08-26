import test_functions as tf
import test_procedures as tp
import messages as mg


improve_count = 0
noImprove_count = 0
counter = len(tp.roster_1617_points) - 1
season_1617 = '2016-2017'
season_1718 = '2017-2018'
TC2A_label = 'TEST CASE 2A'
t2a_pass_msg = 'All players improved'
t2a_fail_msg = ' players had more points in season 2016-2017'
TC2B_label = 'TEST CASE 2B'
t2b_pass_msg = 'The team improved from last season, more points in season 2017-2018'
t2b_fail_msg = 'The team did not improve, more points in season 2016-2017'


print('Executing ' + TC2A_label)

if tp.t2_response_state_1617 and tp.t2_response_state_1718 == True:
    print(mg.response_ok)
else:
    if tp.t2_response_state_1617 == False:
        print(mg.response_nok_suffix + season_1617  + mg.response_nok_preffix)
    else:
        print(mg.response_nok_suffix + season_1718  + mg.response_nok_preffix)

if tp.t2_collect_1617 and tp.t2_collect_1718 == True:
    print(mg.collect_ok)
else:
    if tp.t2_collect_1617 == False:
        print(mg.collect_nok_preffix + season_1617 + mg.collect_nok_suffix)
    else:
        print(mg.collect_nok_preffix + season_1718 + mg.collect_nok_suffix)

if tp.t2_empty_value_1617 or tp.t2_empty_value_1718 == True:
    print(mg.empty_value)

if tp.t2_calculate_1617 and tp.t2_calculate_1718 == True:
    print('Calculating points')
else:
    if tp.t2_calculate_1617 == False:
        print(mg.calculate_nok_preffix + season_1617 + mg.calculate_nok_suffix)
    else:
        print(mg.calculate_nok_preffix + season_1718 + mg.calculate_nok_suffix)

# Test2a Have all the players in the 2016-2017 and 2017-2018 roster improved?

print('Validating ' + TC2A_label)

while counter >= 0:
    if type(tp.roster_1617_points[counter]) and type(tp.roster_1718_points[counter])  == int: #Some goalies have no points
        if tp.roster_1617_points[counter] < tp.roster_1718_points[counter]:
            improve_count = improve_count + 1
        else:
            noImprove_count = noImprove_count + 1
    counter = counter - 1

if noImprove_count > 0:
    tf.test_fail(TC2A_label, str(noImprove_count) + t2a_fail_msg)
else:
    tf.test_pass(TC2A_label, t2a_pass_msg)

#Test2b Has the team improved?

print('Validating ' + TC2B_label)

if tp.team_points_1617 < tp.team_points_1718:
    tf.test_pass(TC2B_label, t2b_pass_msg)
else:
    tf.test_fail(TC2B_label, t2b_fail_msg)
