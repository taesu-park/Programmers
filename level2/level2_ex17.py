#(17) 행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        t = []
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += (arr1[i][k] * arr2[k][j])
            t.append(tmp)
        answer += [t]
    return answer

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))