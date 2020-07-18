#(8) 튜플

def solution(s):
    answer = []
    string = s[2:-2].split("},{")
    string.sort(key=len)
    for i in range(len(string)):
        tmp = string[i].split(",")
        for j in range(len(tmp)):
            if int(tmp[j]) not in answer:
                answer.append(int(tmp[j]))
    return answer