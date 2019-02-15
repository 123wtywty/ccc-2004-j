p_a = 100
p_b = 100
for i in range(int(input())):
    str1 = input()
    list1 = str1.split(' ')
    list1[0], list1[1] = int(list1[0]), int(list1[1])
    if list1[0] > list1[1]:
        p_b -= list1[0]
    elif list1[0] < list1[1]:
        p_a -= list1[1]
    else:
        pass

print(p_a)
print(p_b)
