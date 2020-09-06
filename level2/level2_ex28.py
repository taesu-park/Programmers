#(28) n진수 게임

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    result = []
    num = 0
    while len(result) < t*m:
        result += list(convert(num,n))
        num += 1
    for i in range(t):
        answer += result[i*m+p-1]
    return answer