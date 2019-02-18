class node():

    def __init__(self,name, *value):
        self.parent = []

        self.all_parents = []

        self.sons = []
        self.value = []
        self.value += [i for i in value]
        self.dic = dict()

        self.name = name
        self.dis = 0
        self.all_child = 0

        self.root = self


    def add(self, node):
        self.sons.append(node)

        node.parent = self
        node.dis = self.dis + 1
        node.root = self.root

        node.all_parents = self.all_parents.copy()
        node.all_parents.append(self)




    def delete_son(self, node):
        if node in self.sons:
            self.sons.remove(node)
            return True
        else:
            return False


if __name__ == '__main__':
    root = node('root')

    n1 = node('n1')
    n1.value.append(1)
    root.add(n1)

    s1 = root.sons[0]

    print(s1.all_parents)

    root.delete_son(n1)

    print(root.sons)

    n2 = node('n2')

    n1.add(n2)

    print(root.root)