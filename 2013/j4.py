total_time = int(input())

chores = int(input())
chores_list = []
for i in range(chores):
    chores_list.append(int(input()))

chores_list.sort()


def do(total_time, chores_list, can_do=0):
    time = 0
    for i in range(can_do + 1):
        time += chores_list[i]

    time_left = total_time - time

    if time_left >= 0:
        return do(total_time, chores_list, can_do + 1)

    else:
        return can_do


print(do(total_time, chores_list))
