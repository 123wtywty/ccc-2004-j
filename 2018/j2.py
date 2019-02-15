n = int(input())
y = input()
t = input()
c = 0

for i in range(n):
    y_c = y[i]
    t_c = t[i]
    if (y_c == 'C') and (t_c == 'C'):
        c += 1

print(c)