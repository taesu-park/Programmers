#(22) 영어 끝말잇기

def solution(n, words):
    idx = 1
    answer = [0,0]
    tmp = [words[0]]
    while idx != len(words):
        if words[idx] in tmp or words[idx][0] != tmp[-1][-1]:
            answer = [idx%n + 1,idx//n + 1]
            return answer
        else:
            tmp.append(words[idx])
        idx += 1
    return answer