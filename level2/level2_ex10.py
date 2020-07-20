#(10) 다음 큰 숫자

def solve(nn):
    cnt = 0
    for i in range(len(nn)):
        if nn[i] == '1':
            cnt += 1
    return cnt
def solution(n):
    answer = 0
    nn = format(n,'b')
    cnt = solve(nn)
    while not answer:
        n += 1
        tmp = solve(format(n,'b'))
        if tmp == cnt:
            answer = n
    return answer