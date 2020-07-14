#(6) 라면공장

import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    date = 0
    h = []
    while stock < k:
        for i in range(date,len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h,(-supplies[i],supplies[i]))
                date = i+1
            else:
                break
        stock += heapq.heappop(h)[1]
        answer += 1
    return answer