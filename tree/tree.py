from node import *

tree = []

list1 = [
    ['root', 1, None, [2, 3, 4]],
    ['2', 2, 1, [5]],
    ['3', 3, 1, [6]],
    ['4', 4, 1, [7]],
    ['5', 5, 2, []],
    ['6', 6, 3, []],
    ['7', 7, 4, [8, 9 ]],
    ['8', 8, 7, [10]],
    ['9', 9, 7, []],
    ['10', 10, 8, []]
    ]


for i in list1:
    n = node(i[0], i[1], i[2], i[3])
    tree.append(n)



root = node(list1[0][0], list1[0][1], list1[0][2], list1[0][3])

tree_dic = {}

for i in tree:
    tree_dic[i.id] = i


#print(tree_dic)







#print(root.sons)
