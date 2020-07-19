#(9) 올바른 괄호

def solution(s):
    tmp = dict()
    tmp['('] , tmp[')'] = 0,0
    for i in range(len(s)):
        if tmp.get('(') < tmp.get(')'):
            return False
            break
        tmp[s[i]] += 1
    if tmp['('] != tmp[')']:
        return False
    return True