from node import *


def DFS(tree):
    yield tree
    for i in tree.sons:
        for ii in DFS(i):
            yield ii


class tree():
    def __init__(self, root):

        self.tree = root
        self.bfs = []
        self.dfs = []


    def BFS(self):
        self.bfs = []
        list1 = []
        list1.append(self.tree)
        for i in list1:
            self.bfs.append(i)
            list1 += i.sons
        return self.bfs


    def DFS(self):
        d =  DFS(self.tree)
        self.dfs = []
        for i in d:
            self.dfs.append(i)
        return self.dfs




if __name__ == '__main__':

    list1 = [
        ['n1', 1, None],

        ['n2', 2, 'n1'],
        ['n3', 3, 'n1'],
        ['n4', 4, 'n1'],
        ['n5', 5, 'n2'],
        ['n6', 6, 'n3'],
        ['n7', 7, 'n4'],
        ['n8', 8, 'n7'],
        ['n9', 9, 'n7'],
        ['n10', 10, 'n8']
    ]

    tree1 = dict()

    root = node(list1[0][0], list1[0][1])
    tree1['n1'] = root

    for i in list1[1:]:
        n = node(i[0], i[1])
        tree1[i[0]] = n
        tree1[i[2]].add(n)


    n = tree1['n10']
    print(n.root)
