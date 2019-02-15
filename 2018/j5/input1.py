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





'''
3
2    3    2
0
1   1
'''
