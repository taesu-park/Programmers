#(18) N개의 최소공배수

def solve(a, b):
    ls = []
    if not b % a:
        return b
    else:
        for i in range(1, b + 1):
            ls.append(a * i)
        print(ls)
        for j in range(1, a + 1):
            if b * j in ls:
                return b * j
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    arr.sort()
    tmp = solve(arr[0], arr[1])
    idx = 2
    while idx != len(arr):
        tmp = solve(tmp, arr[idx])
        idx += 1
    return tmp