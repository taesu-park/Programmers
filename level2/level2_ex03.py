answer = 0

def dfs(numbers,target,n):
    global answer
    if n == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return
    else:
        dfs(numbers,target,n+1)
        numbers[n] *= -1
        dfs(numbers,target,n+1)
def solution(numbers, target):
    global answer
    dfs(numbers,target,0)
    return answer

print(solution([1, 1],2))