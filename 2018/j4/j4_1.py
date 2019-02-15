#l = [[1, 3], [2, 9]]
#l = [[4, 3, 1],  [6, 5, 2],  [9, 7, 3]]
all_l = []
s = ''
s.split()
input_ = int(input())
l = []
for i in range(input_):
    input_2 = input()
    input_l = input_2.split(' ')

    for t in range(len(input_l)):
        input_l[t] = int(input_l[t])

    l.append(input_l)

for i in l:
    all_l += i

def turn(l):

    new_l = []
    for n in range(len(l[0])):
        middle_l = []
        for i in l:
            middle_l.append(i[n])
        new_l.append(middle_l)

    new_l.reverse()
    #print(new_l)
    return new_l


# print(new_l)
all_l.sort()
#print(all_l)
new_l = l
while True:
    new_l = turn(new_l)
    if (new_l[0][0] == all_l[0]) and (new_l[-1][-1] == all_l[-1]):
        break

res = ''
for i in new_l:
    for ii in i:
        res += str(ii)
        res += ' '
    res = res[:-1]
    res += '\n'

print(res.strip())