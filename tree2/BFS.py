from tree import *


def BFS(tree):
    list1 = []
    list1.append(tree)
    for i in list1:
        yield i
        list1 += i.sons




for i in BFS(root):
    print(i)