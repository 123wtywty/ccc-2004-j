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