list1 = []
remove_list = []

for i in range(int(input())):
    list1.append(i + 1)

for r in range(int(input())):
    remove_list.append(int(input()))


def remove_(remove, list1, c=1):
    for i in range(len(list1)):
        if c == remove:
            list1[i] = 0
            c = 1
        else:
            c += 1

    list3 = [x for x in list1 if x != 0]

    return list3


list2 = list1.copy()

for n in remove_list:
    list2 = remove_(n, list2)

for f in list2:
    print(f)
