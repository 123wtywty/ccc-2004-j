

#body_code = [[67, 67, 81], [66, 80, 68], [81, 71, 72], [77]]
def uncode(body_code):
    res = []
    for i in body_code:
        for p in i:
            res.append(chr(p))
    res_str = ''
    for i in res:
        res_str += i
    return (res_str)