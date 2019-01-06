def j5_t(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    sx = x2 - x1
    sy = y2 - y1
    p_u = [(0, 0, 1, 0),
           (1, 0, 1, 1),
           (1, 1, 2, 1),
           (2, 1, 2, 0),
           (2, 0, 3, 0)]
    m_l = []
    for l_x1, l_y1, l_x2, l_y2 in p_u:
        l_x1 *= sx // 3
        l_y1 *= sx // 3
        l_x2 *= sx // 3
        l_y2 *= sx // 3
        l_x1 += x1
        l_x2 += x1
        l_y1 += y1
        l_y2 += y1
        m_l.append([l_x1, l_y1, l_x2, l_y2])
    return m_l


def j5_l(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    sy = y2 - y1
    p_u = [(0, 0, 0, 1),
           (0, 1, -1, 1),
           (-1, 1, -1, 2),
           (-1, 2, 0, 2),
           (0, 2, 0, 3)]
    m_l = []
    for l_x1, l_y1, l_x2, l_y2 in p_u:
        l_x1 *= sy // 3
        l_y1 *= sy // 3
        l_x2 *= sy // 3
        l_y2 *= sy // 3
        l_x1 += x1
        l_x2 += x1
        l_y1 += y1
        l_y2 += y1
        m_l.append([l_x1, l_y1, l_x2, l_y2])
    return m_l


def run_(l):
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    list1 = []
    if y1 == y2:
        list1 = (j5_t(l))
    if x1 == x2:
        list1 = (j5_l(l))
    return list1


def j5_Fractals(times, line):
    res_list = []
    if times == 0:
        return line
    else:
        for i in j5_Fractals(times - 1, line):
            res = run_(i)
            res_list += res
        return res_list


def get_point(l):
    out_list1 = []
    for i in l:
        x1, y1, x2, y2 = i
        if x1 == x2:
            c = y2 - y1
            cc = c
            f = 1
            if cc < 0:
                cc *= -1
                f = -1
            for c in range(cc + 1):
                out_list1.append([x1, y1 + c * f])
        elif y1 == y2:
            c = x2 - x1
            cc = c
            f = 1
            if cc < 0:
                cc *= -1
                f = -1
            for c in range(cc + 1):
                out_list1.append([x1 + c * f, y1])
    return out_list1


def main_input():
    str1 = input()
    return str1


def main(str1):
    ll = str1.split(' ')
    i1 = int(ll[0])
    i2 = int(ll[1])
    i3 = int(ll[2])
    l1 = [[0, 0, i2, 0]]
    lines = j5_Fractals(i1, l1)
    all_point = get_point(lines)
    list_res = []
    for ii in all_point:
        if ii[0] == i3:
            list_res.append(ii[1] + 1)
    list11 = set(list_res)
    lll = list(list11)
    lll.sort()
    str2 = ' '.join([str(x) for x in lll])
    return str2


if __name__ == '__main__':
    res = main(main_input())
    print(res)
