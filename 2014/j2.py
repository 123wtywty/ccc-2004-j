input()
str1 = input()
v_a = 0
v_b = 0

for i in str1:
    if i == 'A':
        v_a += 1
    elif i == 'B':
        v_b += 1

if v_a > v_b:
    print('A')
elif v_a < v_b:
    print('B')
else:
    print('Tie')
