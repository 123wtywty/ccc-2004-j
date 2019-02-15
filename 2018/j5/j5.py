from class_tree import tree
from input1 import a
list1 = a

'''
list1 = [[3, 4], [0], [2, 4], [3]]
#list1 = [[2,2,3],[0],[1,1]]
'''

tree_list = []
for i in range(len(list1)):
    tree1 = tree()
    tree1.make(i, list1[i])
    tree_list.append(tree1)


#print(tree_list)


def find(id):
    res = []
    for i in tree_list:
            if i.id == id:
                #print(son)
                res.append(i)
    #print(res)
    return res



def get(tree):
    res = []
    for id in tree.son:
        page2 = find(id)
        #print('get', page2)
        res += page2
    return res


#res = get(tree_list[0])
#print(res)


def get_a(res, c=2):
    r = []
    #print(res)
    for i in res:
        r2 = get(i)
        r += r2
        for ii in r2:
            if ii.son[0] == 0:
                return c

    c += 1
    return get_a(r, c)
    #print(c)

r = get_a([tree_list[0]])
print(r)