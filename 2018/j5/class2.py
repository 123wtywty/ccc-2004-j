import class_tree


class get():

    def __init__(self, tree):
        self.res = []
        self.tree = tree
        self.dd()


    def find(self, id):
        res = []

        for i in self.tree:
            if i.id == id:
                res.append(i)
        return res

    def dd(self, list1):
        list2 = []
        for i in list1:
            page = ''
            for id in i[0][1]:
                if id == 0:
                    self.res.append([0, i[-1] + 1])
                    continue

                page = self.find(id)

                page.append(i[-1] + 1)

                list2.append(page)

        return list2


tree_list = class_tree.tree_list

