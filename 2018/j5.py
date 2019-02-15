def get_input():
    p = int(input())
    list1 = []
    for i in range(p):
        input2 = input()
        need = input2.split(' ')

        need = set(need)
        need = list(need)

        #print(need)
        try:
            need.remove('')
        except:
            pass

        for n in range(len(need)):
            need[n] = int(need[n])

        list1.append(need)

    return list1


a = get_input()

#print(a)

s = 0

for i in range(len(a)):
    l = a.copy()
    l.remove(a[i])


    all = []
    for i1 in l:
        all += i1

    all.append(1)

    all = set(all)
    all = list(all)


    l = []
    for ii in range(len(all)):
        l.append(ii)

    #print(all)
    #print(i+1)
    if (i+1) in all:
        pass
    else:
        s += 1
        print('N')
        break

if s == 0:
    print('Y')


class tree():

    def __init__(self, dis=-1):

        self.dis = dis

    def make(self, i, page_list):
        page_tree = []

        page_tree.append([i + 1, page_list])

        # print(page_tree)
        self.id = i + 1
        self.son = page_list



list1 = a




tree_list = []
for i in range(len(list1)):
    tree1 = tree()
    tree1.make(i, list1[i])
    tree_list.append(tree1)


#print(tree_list)


def find(id):
    res = []
    for i in tree_list:
            if i.id == id:
                #print(son)
                res.append(i)
    #print(res)
    return res



def get(tree):
    res = []
    for id in tree.son:
        page2 = find(id)
        #print('get', page2)
        res += page2
    return res


#res = get(tree_list[0])
#print(res)


def get_a(res, c=2):
    r = []
    #print(res)
    for i in res:
        r2 = get(i)
        r += r2
        for ii in r2:
            if ii.son[0] == 0:
                return c

    c += 1
    return get_a(r, c)
    #print(c)

r = get_a([tree_list[0]])
print(r)

