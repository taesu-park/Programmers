def solution(customer, K):
    answer = []
    wait = []
    for i in range(len(customer)):
        print(answer,wait)
        if customer[i][1] == 1:
            if len(answer) < K:
                answer.append(customer[i][0])                    
            else:
                wait.append(customer[i][0])
        elif customer[i][1] == 0:
            if customer[i][0] in answer:
                answer.remove(customer[i][0])
                if wait:
                    answer.append(wait.pop(0))
            else:
                wait.remove(customer[i][0])
    return sorted(answer)
print(solution([[1, 1], [2, 1], [3, 1], [2, 0], [2, 1]],2))