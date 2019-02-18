from node import *
def x(tree):
    if tree.sons:
        r1 = tree.name
        r2 = x(tree.sons[0])
        r3 = x(tree.sons[1])
        return [r1,r2,r3]
    else:
        return tree.name



list1 = [
    [1,1,0],
    [2,2,1],
    [3,3,1],
    [4,4,2],
    [5,5,2],
    [6,6,3],
    [7,7,3],

]

tree1 = dict()
root = node(list1[0][0], list1[0][1])
tree1[1] = root

for i in list1[1:]:
    n = node(i[0], i[1])
    tree1[i[0]] = n
    tree1[i[2]].add(n)



res1 = x(root)
print(res1)
r = []

def l(list1):
    for i in list1:
        if type(i) == type([]):
            for ii in  l(i):
                yield ii
        else:
            yield i



for i in l(res1):
    r.append(i)

print(r)