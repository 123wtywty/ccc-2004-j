_ = input()
ii = input().split(' ')
l1 = [int(x) for x in ii]

l4 = list(set(l1))
if len(l4) < 2:
    l4 *= 2
p = []

for i in range(len(l4)):
    for n in range(i+1, len(l4)):
        m = l4[i] + l4[n]
        if m not in p:
            p.append(m)

d = {}
for m1 in p:
    l2 = l1.copy()
    while len(l2) >= 2:
        b1 = l2[0]
        n = m1 - b1

        if l2[1:].count(n) >= 1:
            l2.remove(n)
            try:
                d[m1] += 1
            except:
                d[m1] = 1
            else:
                pass

        l2.remove(l2[0])

f_l = []

for k, v in d.items():
    f_l.append([v, k])

f_l.sort(reverse=True)

c = 0

for i3, i4 in f_l:
    if i3 == f_l[0][0]:
        c += 1

print(f_l[0][0], c)
#print(d)