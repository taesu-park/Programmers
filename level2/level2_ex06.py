#(6) 멀쩡한 사각형

def solve(a,b):
    if b == 0:
        return a
    return solve(b,a%b)
def solution(w,h):
    answer = 1
    g = solve(max(w,h),min(w,h))
    answer = w*h-(w+h-g)
    return answer