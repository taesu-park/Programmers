#(3) 입국심사

def solution(n, times):
    answer = 0
    left, right = 0, max(times)*n
    while left <= right:
        mid = (left+right) // 2
        tmp = 0
        for i in range(len(times)):
            tmp += mid // times[i]
        if tmp >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer



def reverse( x: int) -> int:
    if x >= 0:
        return int(str(x)[::-1])
    else:
        tmp = str(x)[1:]
        tmp2 = tmp[::-1]
        result = '-' + tmp2
        return int(result)


print(reverse(1230))