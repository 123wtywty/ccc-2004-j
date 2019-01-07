from j5 import *

def my_print(text):
    pass
    #print(text)

def unit_test_t():
    l1 = [[0, 0, 27, 0]]
    res1 = j5_t(l1[0])
    my_print(res1)
    assert res1 == [[0, 0, 9, 0], [9, 0, 9, 9], [9, 9, 18, 9], [18, 9, 18, 0], [18, 0, 27, 0]]
    l2 = [[9, 3, 6, 3]]
    res2 = j5_t(l2[0])
    my_print(res2)
    assert res2 == [[9, 3, 8, 3], [8, 3, 8, 2], [8, 2, 7, 2], [7, 2, 7, 3], [7, 3, 6, 3]]


unit_test_t()



def unit_test_l():
    l1 = [[9,0,9,9]]
    res1 = j5_l(l1[0])
    my_print(res1)
    assert res1 == [[9, 0, 9, 3], [9, 3, 6, 3], [6, 3, 6, 6], [6, 6, 9, 6], [9, 6, 9, 9]]

    l2 = [[18,0,18,9]]
    res2 = j5_l(l2[0])
    my_print(res2)
    assert res2 == [[18, 0, 18, 3], [18, 3, 15, 3], [15, 3, 15, 6], [15, 6, 18, 6], [18, 6, 18, 9]]



unit_test_l()



def unit_test_j5_Fractals():
    l1 = [[0, 0, 27, 0]]
    res1 = j5_Fractals(2, l1)
    my_print(res1)
    assert res1 == [[0, 0, 3, 0], [3, 0, 3, 3], [3, 3, 6, 3], [6, 3, 6, 0], [6, 0, 9, 0], [9, 0, 9, 3], [9, 3, 6, 3], [6, 3, 6, 6], [6, 6, 9, 6], [9, 6, 9, 9], [9, 9, 12, 9], [12, 9, 12, 12], [12, 12, 15, 12], [15, 12, 15, 9], [15, 9, 18, 9], [18, 9, 18, 6], [18, 6, 21, 6], [21, 6, 21, 3], [21, 3, 18, 3], [18, 3, 18, 0], [18, 0, 21, 0], [21, 0, 21, 3], [21, 3, 24, 3], [24, 3, 24, 0], [24, 0, 27, 0]]



unit_test_j5_Fractals()


def unit_test_get_point():
    l = [[0, 0, 3, 0]]
    res1 = get_point(l)
    my_print(res1)
    assert res1 == [[0, 0], [1, 0], [2, 0], [3, 0]]


unit_test_get_point()

def f_test():
    res1 = main('3 27 5')
    my_print(res1)
    assert res1 == '4 5 6'
    res2 = main('2 27 19')
    my_print(res2)
    assert res2 == '1 4 7'
    res3 = main('4 81 38')
    my_print(res3)
    assert res3 == '37 38 39'


f_test()