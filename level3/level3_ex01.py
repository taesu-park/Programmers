#(1) 네트워크

check = []
def dfs(n,computers,check,x):
    for i in range(n):
        if computers[x][i] == 1 and not check[i]:
            check[i] = 1
            dfs(n,computers,check,i)
def solution(n, computers):
    global check
    answer = 0
    check = [0]*n
    for i in range(n):
        if not check[i]:
            check[i] = 1
            answer += 1
            dfs(n,computers,check,i)
    return answer