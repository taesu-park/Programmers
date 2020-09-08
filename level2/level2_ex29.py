#(29) 압축

def find(msg,idx,tmp,word):
    for i in range(idx,len(msg)):
        tmp = msg[i]
        while idx < len(msg):
            idx += 1
            if idx >= len(msg):
                return idx,tmp
            if tmp+msg[idx] in word:
                tmp += msg[idx]
            else:
                word.append(tmp+msg[idx])
                return idx,tmp
    return idx,tmp
def solution(msg):
    answer = []
    word = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    idx = 0
    while idx < len(msg):
        idx, tmp = find(msg,idx,'',word)
        answer.append(word.index(tmp)+1)
    return answer
