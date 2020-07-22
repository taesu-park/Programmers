result = []
def back(nums,poket,x):
    global result
    if len(poket) == len(nums)//2:
        result.append(poket)
        return
    for i in range(x,len(nums)):
        poket.append(nums[i])
        back(nums,poket[:],i+1)
        poket.pop()
def solution(nums):
    global result
    answer = 0
    back(nums,[],0)
    for i in range(len(result)):
        d = dict()
        for j in range(len(result[i])):
            if result[i][j] not in d:
                d[result[i][j]] = 1
            else:
                d[result[i][j]] += 1
        answer = max(answer,len(d))
    return answer
print(solution([3,1,2,3]))
