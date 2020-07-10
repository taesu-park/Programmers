#(4) 124 나라의 숫자

def solution(n):
    answer = ''
    num = [1,2,4]
    while n > 0:
        n -= 1
        answer = str(num[n%3]) + answer
        n = n//3
    return answer