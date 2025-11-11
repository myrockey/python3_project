#!/usr/bin/python3

def average2(vals):
    '''
    >>> print(average2([20,30,100]))
    50.0
    '''
    return sum(vals)/len(vals)

import doctest
doctest.testmod() # 自动验证嵌入测试
print('unit test...')
'''
结果：
unit test...
'''
