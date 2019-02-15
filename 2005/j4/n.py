import math


def get_input():
    room_wide = int(input())
    room_height = int(input())
    cut_out_wide = int(input())
    cut_out_height = int(input())
    step = int(input())
    return room_wide, room_height, cut_out_wide, cut_out_height, step


def get_room(size):
    room_wide = size[0]
    room_height = size[1]
    cut_out_wide = size[2]
    cut_out_height = size[3]
    list1 = []
    for i1 in range(cut_out_height):
        line = []
        for n1 in range(cut_out_wide):
            line.append(0)
        for n2 in range(room_wide - cut_out_wide * 2):
            line.append(1)
        for n3 in range(cut_out_wide):
            line.append(0)
        list1.append(line)

    for i2 in range(room_height - cut_out_height * 2):
        line = [1]
        line *= room_wide
        list1.append(line)

    for i3 in range(cut_out_height):
        line = []
        for n1 in range(cut_out_wide):
            line.append(0)
        for n2 in range(room_wide - cut_out_wide * 2):
            line.append(1)
        for n3 in range(cut_out_wide):
            line.append(0)
        list1.append(line)
    for i in list1:
        print(i)
    return list1


def able_point(start, room):
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


def main(get_all_input):
    get_input = get_all_input[:-1]
    step = get_all_input[-1]

    if get_input[2] * 2 < get_input[0]:
        start = [get_input[2] + 1, 1]
    else:
        start = [0, 0]

    new_room = get_room(get_input)

    step_list = []

    step_list.append(start)
    now_point = start

    d = [1, 0]
    middle_point = [get_input[0] / 2, get_input[1] / 2]

    def get_distance(p1, p2):
        line1 = abs(p1[0] - p2[0])
        line2 = abs(p1[1] - p2[1])
        s = line1 ** 2 + line2 ** 2
        return math.sqrt(s)

    for i in range(step):
        able, new_room = able_point(now_point, new_room)
        # print('able:', able)
        next_point1 = [now_point[0] + d[0], now_point[1] + d[1]]
        # print('next_point:', next_point1)
        if (next_point1 in able) and (len(able) == 2):

            now_point = next_point1


        elif len(able) == 1:
            d = [able[0][0] - now_point[0], able[0][1] - now_point[1]]
            now_point = able[0]

        elif len(able) == 3:
            distance_list = []
            for i in able:
                distance = get_distance(i, middle_point)
                distance_list.append([distance, i])
            distance_list.sort(key=lambda x: x[0], reverse=True)
            d = [distance_list[0][1][0] - now_point[0], distance_list[0][1][1] - now_point[1]]

            now_point = distance_list[0][1]

        step_list.append(now_point)

    return step_list


def run():
    all_input = get_input()
    res = main(all_input)
    for i in res:
        print(i)


run()
