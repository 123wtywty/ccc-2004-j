from tree import *


def DFS(tree):
    yield tree
    for i in tree.sons:
        for ii in DFS(i):
            yield ii



for i in DFS(root):
    print(i.name)
