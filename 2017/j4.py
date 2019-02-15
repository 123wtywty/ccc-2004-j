def clock(hour, min1, min2):
    if min2 == 10:
        min1 += 1
        min2 = 0

    if min1 == 6:
        hour += 1
        min1 = 0

    if hour == 13:
        hour = 1

    return hour, min1, min2


def times(time_):
    list1 = [12, 0, 0]
    c = 0
    for i in range(time_):

        list1 = clock(list1[0], list1[1], list1[2] + 1)

        str1 = ''.join([str(x) for x in list1])

        diff = int(str1[0]) - int(str1[1])
        t = 0
        for ii in range(1, len(str1) - 1):
            if diff != (int(str1[ii]) - int(str1[ii + 1])):
                t += 1

        if t == 0:
            c += 1

    return c


time_ = int(input())

half_day = time_ // (12 * 60)
left_day = time_ % (12 * 60)

t1 = times(12 * 60) * half_day
t2 = times(left_day)

print(t1 + t2)
