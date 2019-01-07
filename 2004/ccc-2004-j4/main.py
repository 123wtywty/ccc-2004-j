from header import *
from body import *
from uncode import *
head_text = input()
body_text = input()

head_code = header_code(head_text)
body_code = body_code(head_code, body_text)
res = uncode(body_code)

print(res)