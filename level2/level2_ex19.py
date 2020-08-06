#(19) JadenCase 문자열 만들기

def solution(s):
    answer = ''
    check = True
    for i in range(len(s)):
        if check:
            answer+=s[i].upper()
            check = False
        else:
            answer += s[i].lower()
        if s[i] == ' ':
            check = True
    return answer