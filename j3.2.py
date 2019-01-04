def my_print(x, end="\n"):
    #print(x, end=end)
    pass

def my_input():
    i1 = int(input())
    i2 = int(input())
    list3 = []
    list4 =[]
    for i in range(i1):
        i3 = input().rstrip()
        list3.append(i3)
    for i in range(i2):
        i4 = input().rstrip()
        list4.append(i4)
    return list3, list4


def my_run(data):
    outupt = []

    l1, l2 = data
    for adj in l1:
        for noun in l2:
            o = '{} as {}'.format(adj, noun)
            outupt.append(o)
            #print(f'{adj} as {ii2}')

    outuptstr = '\n'.join(outupt)

    return outuptstr


def my_unit_test():

    pass


def my_func_test():
    list3 = ['a','b']
    list4 = ['c','d']
    input_=(list3,list4)
    r = my_run(input_)
    #print(r)
    assert 'b as c' in r
    assert 'c as b' not in r
    return


def my_main_test():
    #my_print("==unit=="*10)
    my_unit_test()
    #my_print("==func==" * 10)
    my_func_test()

my_main_test()

def main():
    input1 = my_input()
    res = my_run(input1)
    print(res)
main()