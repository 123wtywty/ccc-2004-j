class tree():

    def __init__(self, dis=-1):

        self.dis = dis

    def make(self, i, page_list):
        page_tree = []

        page_tree.append([i + 1, page_list])

        # print(page_tree)
        self.id = i + 1
        self.son = page_list


'''
tree_list = []

list1 = [[3, 4], [0], [2, 4], [3]]

for i in range(len(list1)):
    tree1 = tree()
    tree1.make(i, list1[i])
    tree_list.append(tree1)

root = tree_list[0]

#tree_list = tree_list[1:]




def find(id, l):
    res = []
    for i in l:
        for son in i.son:
            #print(son)
            if son == id:
                #print(son)
                res.append(i)

    return res




def get(tree, tree_list):
    list1 = []
    for i in tree.son:
        print('i', i)
        page = find(i, tree_list)
        #page.dis = 1
        print('get', page[0].son)
        list1 += page
    return list1


list1 = get(root, tree_list)

print(list1)



for i in list1:
    print('-------')

    print(i.son)

res = []
for t in list1:
        print('ti', t.son)
        l = get(t, tree_list)
        res += l

print(res)

for i in res:
        print('-------')
        print('*')
        print(i.id)
        print(i.son)

'''