import test_functions as tf
import Test1, Test2, Test3

# Test summary using the # of test cases pass, fail and not executed from Test1 Test2 and Test3
t_pass = Test1.t_pass + Test2.t_pass + Test3.t_pass
t_fail = Test1.t_fail + Test2.t_fail + Test3.t_fail

tf.test_summary(t_pass,t_fail)
