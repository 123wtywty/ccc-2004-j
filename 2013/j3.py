y_input = int(input())



def c(str1):
    l_s = []
    for i in str1:
        if i not in l_s:
            l_s.append(i)
        else:
            return 'F'
    return 'T'

while True:
    y_input += 1
    res = c(str(y_input))
    if res == 'T':
        print(y_input)
        break

    else:
        pass
