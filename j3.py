i1 = input()
i2 = input()
i1 = int(i1)
i2 = int(i2)
list1 = []
list2 = []
for i in range(i1):
    i3 = input()
    
    list1.append(i3)

for i in range(i2):
    i4 = input()
    list2.append(i4)

print(list1)
for ii1 in list1:
    for ii2 in list2:
        print(f'{ii1} as {ii2}')

