page_list = [[3,4], [0], [2,4], [3]]


page_tree = []
page_tree2 = []

for i in range(len(page_list)):
    page_tree.append([i+1, page_list[i]])

print(page_tree)


'''
for id in range(1, len(page_tree)):

    for son in range(len(page_tree)):

        if page_tree[id][0] in page_tree[son][1]:
            print(page_tree[id],(page_tree[son][0]))
            #page_tree2.append([page_tree[id].append(page_tree[son][0])])


'''
#print(page_tree2)