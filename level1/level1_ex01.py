#(1) 비밀지도

def solution(n, arr1, arr2):
    answer = []
    a1, a2 = [], []
    for i in range(len(arr1)):
        tmp1, tmp2 = format(arr1[i], 'b').zfill(n), format(arr2[i], 'b').zfill(n)
        a1.append(tmp1)
        a2.append(tmp2)
    for i in range(len(a1)):
        tmp = ''
        for j in range(len(a1[i])):
            if a1[i][j] == a2[i][j]:
                tmp+=(a1[i][j])
            else:
                if a1[i][j] == '1' or a2[i][j] == '1':
                    tmp+='1'
                else:
                    tmp+='0'
        answer.append(tmp)
    for i in range(len(answer)):
        answer[i] = answer[i].replace('1','#').replace('0',' ')
    return answer