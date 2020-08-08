#(20) 짝지어 제거하기

def solution(s):
    answer = 0
    tmp = []
    for i in range(len(s)):
        if not tmp:
            tmp.append(s[i])
        elif tmp[-1] == s[i]:
            tmp.pop()
        else:
            tmp.append(s[i])
    if not tmp:
        answer = 1
    return answer