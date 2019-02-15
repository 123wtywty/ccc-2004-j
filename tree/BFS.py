from tree import *

def BFS(root, tree, res=[]):
    list1 = root.sons
    res.append(root)
    while len(list1) > 0:
        n = tree[list1[0]]
        res.append(n)
        list1.extend(n.sons)
        list1 = list1[1:]

    return res



r = BFS(root, tree_dic)
print(r)

for i in r:
    print(i.id)



