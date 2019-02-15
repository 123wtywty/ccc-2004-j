def able_point(start,  room):
    f_r, f_c = start[1], start[0]
    able = []
    action1 = [1, 0]
    action2 = [-1, 0]
    action3 = [0, 1]
    action4 = [0, -1]
    action = [action1, action2, action3, action4]
    room[f_r - 1][f_c - 1] = 0
    for i in action:
        if (f_r - 1 - i[0] >= 0) and (f_c - 1 - i[1] >= 0):
            try:
                s = room[f_r - 1 - i[0]][f_c - 1 - i[1]]
            except:
                pass
            else:
                if s == 1:
                    able.append([f_c - i[1], f_r - i[0]])
    return able, room


if __name__ == '__main__':
    from get_room import *
    size = [10, 8, 3, 2]
    a = get_room(size)
    for i in a:
        print(i)

    start = [1, 4]
    r = 1
    c = 4
    # print(a[1 - 1][4 - 1])
    p, new_room = able_point([c, r], a)
    print(p)
    for i in new_room:
        print(i)

    p, new_room = able_point([5, 1], new_room)
    print(p)
    for i in new_room:
        print(i)
