#print('Enter the current year:')
i = input()
#print('Enter a future year:')
i2 = input()

i = int(i)
i2 = int(i2)

while i <= i2:
    print('All positions would change in year {}'.format(i))
    i += 60
