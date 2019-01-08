

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

    return list1

if __name__ == '__main__':
    size = [10, 8, 3, 2]
    room = get_room(size)
    for i in room:
        print(i)