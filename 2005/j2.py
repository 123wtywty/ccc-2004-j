def divisor(x):
    n = 1
    list = []
    while n < x:
        n += 1
        q = x % n
        if q == 0:
            list.append(n)
            x /= n
            n -= 1
            continue
        else:
            pass
    return list


def my_print(text):
    print(text)
    pass


def get_input():
    my_print('Enter lower limit of range')
    lower_ = int(input())
    my_print('Enter upper limit of range')
    upper_ = int(input())
    return lower_, upper_


def main(lower_, upper_):
    c = 0
    for i in range(lower_, upper_+1):
        res = divisor(i)
        if len(res) == 2:
            c += 1
    return c


def res_print(lower_, upper_, c):
    res_str = 'The number of RSA numbers between {} and {} is {}'.format(lower_, upper_, c)
    print(res_str)

def run():
    input1 = get_input()
    c = main(input1[0], input1[1])
    res_print(input1[0], input1[1], c)

run()