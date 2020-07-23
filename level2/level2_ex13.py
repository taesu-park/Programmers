#(13) 숫자의 표현

def solution(n):
    answer = 1
    idx = 1
    while idx <= n//2 + 2:
        tmp = 0
        for i in range(idx,(n//2)+2):
            tmp += i
            if tmp == n:
                answer += 1
                break
            if tmp > n:
                break
        idx += 1
    return answer