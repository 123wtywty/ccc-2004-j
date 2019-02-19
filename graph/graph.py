class node():
    def __init__(self, name, value=None):
        self.name = name
        self.value = [value]
        self.dic = dict()
        self.tag = False
        self.connect = []


class graph():

    def __init__(self):
        self.dic = dict()

    def connect(self, a, b):

        if a not in self.dic:
            self.dic[a] = node(a)

        if b not in self.dic:
            self.dic[b] = node(b)

        if b not in self.dic[a].connect:
            self.dic[a].connect.append(b)
        if a not in self.dic[b].connect:
            self.dic[b].connect.append(a)

    def exist(self, a):
        if a in self.dic:
            return True
        else:
            return False

    def find_path(self, a, b):
        for k, v in self.dic.items():
            v.tag = False
            v.dic['dis'] = []
        if self.exist(a) and self.exist(b):
            pass
        else:
            return False

        l1 = []

        n_a = self.dic[a]

        n_a.dic['dis'] = []

        l1.append(a)

        while l1:
            i = l1.pop(0)

            n = self.dic[i]

            if n.tag:
                continue
            n.tag = True

            if i != b:

                for t in n.connect:
                    n2 = self.dic[t]
                    if not n2.tag:
                        n2.dic['dis'] = []
                        n2.dic['dis'] += n.dic['dis']
                        n2.dic['dis'].append(i)
                        l1.append(t)

            else:
                self.dic[b].dic['dis'].append(b)
                # print(type(self.dic[b]))
                return self.dic[b]



    def all_connect(self, ):
        for k, v in self.dic.items():
            v.tag = False
        keys1 = []
        for ii in self.dic.keys():
            keys1.append(ii)
        fist_node = keys1[0]


        l1 = [fist_node]
        l2 = [fist_node]

        while l1:
            i = l1.pop(0)
            n = self.dic[i]

            if n.tag:
                continue
            n.tag = True

            for t in n.connect:
                n2 = self.dic[t]
                if not n2.tag:
                    l1.append(t)
                    l2.append(t)


        for i in self.dic.keys():
            if i not in l2:
                return False

        return True


if __name__ == '__main__':
    g = graph()
    g.connect(1, 2)
    g.connect(2, 3)
    g.connect(3, 4)
    # g.connect(4, 1)

    g.connect(1, 9)
    g.connect(8, 4)
    g.connect(1, 8)
    for k, v in g.dic.items():
        pass
        #print(k, '   ', v.connect)

    b = g.find_path(1, 3)
    #print(b.dic['dis'])

    c = g.find_path(1, 4)
    #print(c.dic['dis'])

    g.connect(100, 200)

    t = g.all_connect()
    print(t)