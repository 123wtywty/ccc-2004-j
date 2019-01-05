
def j5_t(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    sx = x2-x1
    sy = y2-y1
    p_u = [(0, 0, 1, 0),
           (1, 0, 1, 1),
           (1, 1, 2, 1),
           (2, 1, 2, 0),
           (2, 0, 3, 0)]
    m_l = []
    for l_x1, l_y1, l_x2, l_y2 in p_u:
        l_x1 *= sx//3
        l_y1 *= sx//3
        l_x2 *= sx//3
        l_y2 *= sx//3
        l_x1 += x1
        l_x2 += x1
        l_y1 += y1
        l_y2 += y1
        m_l.append([l_x1, l_y1, l_x2, l_y2])
    return m_l


def j5_b(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    sx = x2-x1
    p_u = [(0, 0, -1, 0),
           (-1, 0, -1, -1),
           (-1, -1, -2, -1),
           (-2, -1, -2, -0),
           (-2, -0, -3, -0)]
    m_l = []
    for l_x1, l_y1, l_x2, l_y2 in p_u:
        l_x1 *= -sx//3
        l_y1 *= -sx//3
        l_x2 *= -sx//3
        l_y2 *= -sx//3
        l_x1 += x1
        l_x2 += x1
        l_y1 += y1
        l_y2 += y1
        m_l.append([l_x1, l_y1, l_x2, l_y2])
    return m_l


def j5_l(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    sy = y2-y1
    p_u = [(0, 0, 0, 1),
           (0, 1, -1, 1),
           (-1, 1, -1, 2),
           (-1, 2, 0, 2),
           (0, 2, 0, 3)]
    m_l = []
    for l_x1, l_y1, l_x2, l_y2 in p_u:
        l_x1 *= sy//3
        l_y1 *= sy//3
        l_x2 *= sy//3
        l_y2 *= sy//3
        l_x1 += x1
        l_x2 += x1
        l_y1 += y1
        l_y2 += y1
        m_l.append([l_x1, l_y1,l_x2, l_y2])
    return m_l


def j5_r(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    sy = y1-y2
    p_u = [(0,0,0,-1),
           (0,-1,1,-1),
           (1,-1,1,-2),
           (1,-2,0,-2),
           (0,-2,0,-3)]
    m_l = []
    for l_x1, l_y1, l_x2, l_y2 in p_u:
        l_x1 *= sy//3
        l_y1 *= sy//3
        l_x2 *= sy//3
        l_y2 *= sy//3
        l_x1 += x1
        l_x2 += x1
        l_y1 += y1
        l_y2 += y1
        m_l.append([l_x1, l_y1, l_x2, l_y2])
    return m_l


str1 = input()
ll = str1.split(' ')
i1 = int(ll[0])
i2 = int(ll[1])
i3 = int(ll[2])



def run_(l):

    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    list1 = []
    if y1 == y2:
        if x1 < x2:
            list1=(j5_t(l))

        elif x1 > x2:
            list1=(j5_b(l))
    if x1 == x2:
        if y1 < y2:
            list1=(j5_l(l))
        elif y1 > y2:
            list1=(j5_r(l))

    return list1

def main_re_(t, l):
    l1 = l
    l2 = []
    l3 = []
    for i in range(t):
        for i in l1:
            res1 = run_(i)
            for p in res1:
                l2.append(p)
            l3 = l2.copy()
            l1 = l2.copy()
        l2 = []
    if t == 0:
        return l
    return l3
l1 = [[0,0, i2,0]]
a = main_re_(i1 ,l1)

def get_point(l):
    out_list1 = []
    for i in l:
        x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
        if x1 == x2:
            c = y2 - y1
            cc = c
            f = 1
            if cc < 0:
                cc *= -1
                f = -1
            for i in range(cc+1):
                out_list1.append([x1, y1+i*f])

        elif y1 == y2:
            c = x2 - x1
            cc = c
            f = 1
            if cc < 0:
                cc *= -1
                f = -1
            for i in range(cc+1):
                out_list1.append([x1+i*f, y1])


    return out_list1



def get_all_point(l):
    o = []
    for i in l:
        g = get_point(i)
        for ii in g:
            o.append(ii)

    return o

oooo = get_point(a)

list_res = []
for ii in oooo:
        if ii[0] == i3:
            list_res.append(ii[1]+1)
list11 = set(list_res)
lll = list(list11)
lll.sort()


out_str = ''

for i in lll:
    out_str += str(i)
    out_str += ' '

out_str = out_str[0:-1]
print(out_str)
