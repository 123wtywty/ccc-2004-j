from j4_2 import *

def code_test():
    assert code('A', 'B') == 'B'
    assert code('D', 'B') == 'E'
    assert code('B', 'A') == 'B'

code_test()





def my_func_test():
    key = 'ACT'
    message = 'BANANA & PEEL'
    res = run(key, message)
    print(res)
    assert res == 'BCGAPTPGXL'
my_func_test()