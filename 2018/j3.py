input_ = input()

l = input_.split(' ')
for i in range(len(l)):
    l[i] = int(l[i])


def g(l):
    p = [0, l[0], l[0] + l[1], l[0] + l[1] + l[2], l[0] + l[1] + l[2] + l[3]]
    pp = []
    pp.append(p)
    for x in range(len(l)):
        middle = []
        for i in range(len(p)):
            middle_i = abs(p[i] - p[x + 1])
            middle.append(middle_i)
        pp.append(middle)

    return pp


res = ''
for i in g(l):
    for r in i:
        res += str(r)
        res += ' '
    res.strip()
    res += '\n'

print(res.strip())
