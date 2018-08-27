import test_functions as tf
import Test1, Test2, Test3

t_pass = Test1.t_pass + Test2.t_pass + Test3.t_pass
t_fail = Test1.t_fail + Test2.t_fail + Test3.t_fail
t_noexec = Test1.t_noexec + Test2.t_noexec + Test3.t_noexec

tf.test_summary(t_pass,t_fail,t_noexec)
