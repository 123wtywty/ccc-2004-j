from tree import *


def BFS(tree):
    list1 = []
    list1.append(tree)
    while list1:
        i = list1.pop(0)
        yield i
        list1 += i.sons


for i in BFS(root):
    print(i.name)
