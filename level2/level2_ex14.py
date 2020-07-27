#(14) 최댓값과 최솟값

def solution(s):
    answer = ''
    answer += str(min(list(map(int,s.split(" "))))) + ' '+ str(max(list(map(int,s.split(" ")))))
    return answer