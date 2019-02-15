p1 = input()
p1 = p1.split()
p1 = [int(x) for x in p1]

p2 = input()
p2 = p2.split()
p2 = [int(x) for x in p2]

battery = int(input())

distence = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if battery >= distence:
    c = (battery - distence) % 2

    if c == 0:
        print('Y')
    else:
        print('N')
else:
    print('N')

