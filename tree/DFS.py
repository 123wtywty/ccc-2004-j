from tree import *


def DFS(root, tree, res=[]):
    res = []
    res.append(root)
    for i in root.sons:
        print(i)
        s = tree[i]
        res += DFS(s, tree)

    return res


res = DFS(root, tree_dic)
print(res)

for i in res:
    print(i.id)
