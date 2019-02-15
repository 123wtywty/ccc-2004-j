a = []
for t in range(4):
    i = input()
    i = int(i)
    a.append(i)

if ((a[0] == 8) or (a[0] == 9)) and (a[1] == a[2]) and ((a[3] == 8) or (a[3] == 9)):
    print('ignore')

else:
    print('answer')
