#(2) 예산

answer = 0

def binary_search(budgets, M, left, right):
    global answer
    if left > right:
        return
    else:
        tmp = 0
        mid = (left + right) // 2
        for i in budgets:
            if i < mid:
                tmp += i
            else:
                tmp += mid
        if tmp >= M:
            binary_search(budgets,M,left,mid-1)
        else:
            answer = mid
            binary_search(budgets,M,mid+1,right)
    return answer

def solution(budgets, M):
    global answer
    answer = binary_search(budgets, M, 0, max(budgets))
    return answer