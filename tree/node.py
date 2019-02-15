class node:
    def __init__(self, value, id, parent, sons):
        self.value = value
        self.id = id
        self.parent = parent
        self.sons = sons



if __name__ == '__main__':
    n1 = node('root', 1, None, [2, 3, 4])


    print(n1.sons)

    for i in n1.sons:
        print(type(i))