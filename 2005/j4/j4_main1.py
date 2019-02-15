

class j4():

    def __init__(self):
        self.get_input()
        self.room = self.get_room()


    def get_input(self):
        self.room_wide = int(input())
        self.room_height = int(input())
        self.cut_out_wide = int(input())
        self.cut_out_height = int(input())
        self.step = int(input())

    def get_room(self):
        room_wide = self.room_wide
        room_height = self.room_height
        cut_out_wide = self.cut_out_wide
        cut_out_height = self.cut_out_height
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

    def main(self):
        get_input = [10, 8, 3, 2]

        if get_input[2] * 2 < get_input[0]:
            start = [get_input[2] + 1, 1]
        else:
            start = [0, 0]

        room = get_room(get_input)

        step_list = []

        step_list.append(start)
        now_point = start

        d = [1, 0]
        middle_point = [get_input[0] / 2, get_input[1] / 2]
        new_room = room

        def get_distance(p1, p2):
            line1 = abs(p1[0] - p2[0])
            line2 = abs(p1[1] - p2[1])
            s = line1 ** 2 + line2 ** 2
            return math.sqrt(s)

        for i in range(15):
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

        return step_list[-1]


a = j4()
a.get_input()
a.get_room()