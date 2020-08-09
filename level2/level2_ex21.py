#(21) 소수 만들기

answer = 0
def isSosu(n):
    for i in range(2,int(n**0.5)+1):
        if not n % i:
            return False
    return True
def back(nums,cnt,tmp,check,x):
    global answer
    if cnt == 3:
        if isSosu(tmp):
            answer += 1
        return
    for i in range(x,len(nums)):
        if not check[i]:
            check[i] = 1
            back(nums,cnt+1,tmp+nums[i],check,i)
            check[i] = 0
def solution(nums):
    global answer
    back(nums,0,0,[0]*len(nums),0)
    return answer