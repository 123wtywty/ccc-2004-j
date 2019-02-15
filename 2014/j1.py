angles = []
for i in range(3):
    angles.append(int(input()))

all = angles[0] + angles[1] + angles[2]
if all != 180:
    print('Error')
else:
    set_ = set(angles)
    if len(set_) == 1:
        print('Equilateral')
    elif len(set_) == 2:
        print('Isosceles')
    else:
        print('Scalene')
