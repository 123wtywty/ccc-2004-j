
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