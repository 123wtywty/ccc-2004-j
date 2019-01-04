from j4 import *
import re
def my_unit_test_header():
    input1 = 'CAT'
    o = header_code(input1)
    assert len(o) == len(input1)
    for i in o:
        assert i <= 26

    if input1 == 'CAT':
        assert o == [2, 0, 19]

    #print(o)

my_unit_test_header()

def my_unit_test_body():
    o = [2, 0, 19]
    str1 = 'BANANA & PEEL'
    code = body_code(o, str1)
    assert len(code) <= len(str1)/len(o)
    for i in code:
        for e in i:
            assert (e >= 65) and (e <= 65 + 25)
    if (o == [2, 0, 19]) and (str1 == 'BANANA & PEEL'):
        assert code == [[68, 65, 71], [67, 78, 84], [82, 69, 88], [78]]


my_unit_test_body()


def my_unit_test_uncode():
    code = [[68, 65, 71], [67, 78, 84], [82, 69, 88], [78]]
    res = uncode(code)
    re_res = re.findall('[A-Z]+', res)
    assert res == re_res[0]
    if code == [[68, 65, 71], [67, 78, 84], [82, 69, 88], [78]]:
        assert res == 'DAGCNTREXN'

my_unit_test_uncode()


def my_func_test():
    input1 = 'TRICKY'
    input2 = 'I LOVE PROGRAMMING!'
    header = header_code(input1)
    body = body_code(header, input2)
    res = uncode(body)
    assert res == 'BCWXONKFOTKKFZVI'

my_func_test()