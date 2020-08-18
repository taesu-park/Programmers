#(24) 예상 대진표

def solution(n,a,b):
    answer = 1
    l_idx,r_idx = 0,0
    if a%2:
        l_idx = a//2 + 1
    else:
        l_idx = a//2
    if b%2:
        r_idx = b//2 + 1
    else:
        r_idx = b//2
    while l_idx != r_idx:
        if l_idx%2:
            l_idx = l_idx//2 + 1
        else:
            l_idx = l_idx//2
        if r_idx%2:
            r_idx = r_idx//2 + 1
        else:
            r_idx = r_idx//2
        answer += 1
    return answer

print(solution(8,4,7))