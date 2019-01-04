import re

#header = 'ABCDE'
def header_code(text):
    header_list = re.findall('[A-Z]', text)
    header_list_code = []
    for i in header_list:
        code = ord(i)
        header_list_code.append(code-65)

    return (header_list_code)

#print(header_code(header))



#header_code = [1,2,3]

#body_text = 'BANANA & PEEL'

def body_code(header_code, body_text):
    body_list = re.findall('[A-Z]', body_text)
    body_list_code = []
    for i in body_list:
        code = ord(i)
        body_list_code.append(code)


    #print(body_list)


    body_list_code_pack = []
    middle = []
    c = 0
    for i in body_list_code:
        c += 1
        middle.append(i)
        if c == len(header_code):
            body_list_code_pack.append(middle)
            middle = []
            c = 0

    if len(middle) > 0:
        body_list_code_pack.append(middle)

    #print(body_list_code_pack)

    for i in body_list_code_pack:
        for p in range(len(i)):
            #print(header_code[p] + i[p])
            new_code = header_code[p] + i[p]
            if new_code > 90:
                new_code -= 26
            i[p] = new_code

    return (body_list_code_pack)

def uncode(body_code):
    res = []
    for i in body_code:
        for p in i:
            res.append(chr(p))
    res_str = ''
    for i in res:
        res_str += i
    return (res_str)




head_text = input()
body_text = input()

head_code = header_code(head_text)
body_code = body_code(head_code, body_text)
res = uncode(body_code)

print(res)