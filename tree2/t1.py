def run(str1):
    l1 = str1.split(' ')

    s1 = []

    def c(s):
        if (s == '-') or (s == '+'):
            return True
        else:
            return False

    def combine(s1):

        if len(s1) >= 3:
            if (c(s1[-3])) and ((not c(s1[-2])) and (not c(s1[-1]))):
                s1[-3:] = [[s1[-3], s1[-2], s1[-1]]]
                combine(s1)

        return s1

    while l1:
        s1.append(l1.pop(0))

        s1 = combine(s1)

    # print(s1)

    def get_res(t):

        if type(t) != type([]):
            return t

        else:

            r1 = t[0]
            r2 = t[1]
            r3 = t[2]

            return [get_res(r2), get_res(r3), r1]

    # print(get_res(s1[0]))
    def l(list1):
        for i in list1:
            if type(i) == type([]):
                for ii in l(i):
                    yield ii
            else:
                yield i

    res1 = []
    if len(s1) == 1:
        s1 = s1[0]
    for i in l(get_res(s1)):
        res1.append(i)

    print(' '.join(res1))


def get_input():
    l = []
    while True:
        i = input()
        if i != '0':
            l.append(i)
        else:
            break
    return l


i = get_input()
for ii in i:
    run(ii)
