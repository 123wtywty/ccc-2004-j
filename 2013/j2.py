w_l = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

w_input = input()
c = 0
for i in w_input:
    if i in w_l:
        pass
    else:
        c += 1

if c == 0:
    print('YES')
else:
    print('NO')
    