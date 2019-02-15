# page_list = [[3,4], [0], [2,4], [3]]
page_list = [[2, 2, 3], [0], [1, 1]]


page_list2 = [[1, [3, 4]],
              [2, [0]],
              [3, [2, 4]],
              [4, [3]]]

root = [1, [3, 4]]


# root = [[1, [3, 4]], 1]

def find(id, l):
    res = []
    for i in l:
        if i[0] == id:
            res.append(i)
    return res


list1 = []

for i in root[1]:
    page = find(i, page_list2)
    page.append(1)
    list1.append(page)

print(list1)

# list2 = []
res = []


def dd(list1):
    list2 = []
    for i in list1:
        page = ''
        for id in i[0][1]:
            if id == 0:
                res.append([0, i[-1] + 1])
                continue

            page = find(id, page_list2)

            page.append(i[-1] + 1)

            list2.append(page)

    return list2


list2 = dd(list1)

print(dd(list1))

print(dd(list2))

print(dd(dd(list2)))

print(res)
# print(find(3, page_list2))
