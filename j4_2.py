import re

def get_input():
    key = input()
    message = input()
    return key, message


def manage_input(key, message):
    list_key = re.findall('[A-Z]', key)
    list_message = re.findall('[A-Z]', message)
    return list_key, list_message

def code(key, message):
    key_code = ord(key) - 65
    message_code = ord(message)
    res = key_code + message_code
    if res > 90:
        res -= 26

    return chr(res)


def manage(list_key, list_message):
    res = ''
    for i in range(len(list_message)):
        key_ = list_key[i%len(list_key)]
        message_ = list_message[i]
        res += code(key_, message_)
    return res


def run(key, message):
    list_key, list_message = manage_input(key, message)
    return manage(list_key, list_message)


def main():
    key, message = get_input()
    print(run(key, message))

#main()