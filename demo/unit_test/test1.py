#!/usr/bin/python3

def average2(vals):
    '''
    >>> print(average2([20,30,100]))
    60.0
    '''
    return sum(vals)/len(vals)

import doctest
doctest.testmod() # 自动验证嵌入测试
print('unit test...')

# 输出结果：
# File "d:\projects\python3_project\demo\unitest\test1.py", line 5, in __main__.average2
# Failed example:
#     print(average2([20,30,100]))
# Expected:
#     60.0
# Got:
#     50.0
# **********************************************************************
# 1 item had failures:
#    1 of   1 in __main__.average2
# ***Test Failed*** 1 failure.
# unit test...