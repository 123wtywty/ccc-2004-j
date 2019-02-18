from tree import *

p1 = 'n6'
p2 = 'n10'

n1 = tree1[p1]
n2 = tree1[p2]

parents_of_n1 = n1.all_parents
parents_of_n1.reverse()
parents_of_n2 = n2.all_parents

path = [n1]

for i in parents_of_n1:
    if i not in parents_of_n2:
        path.append(i)
        parents_of_n1.pop(0)

path.append(parents_of_n1[0])

i = parents_of_n2.index(parents_of_n1[0])

path += parents_of_n2[i + 1:]
path.append(n2)

for i in path:
    print(i.name)
