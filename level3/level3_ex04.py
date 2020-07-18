#(4) 단어 변환

def bfs(begin,target,words,answer,visit):
    start = [begin]
    while start:
        print(start)
        if target in start:
            return answer
        tmp = start.pop()
        for i in range(len(words)):
            cnt = 0
            for j in range(len(words[i])):
                if words[i][j] != tmp[j]:
                    cnt += 1
            if cnt == 1:
                if not visit[i]:
                    visit[i] = 1
                    start.append(words[i])
        answer += 1
def solution(begin, target, words):
    answer = 0
    visit = [0]*len(words)
    if target not in words:
        return 0
    answer = bfs(begin,target,words,answer,visit)
    return answer

print(solution("hit","cog",["hot", "hut","dot", "dog", "lot", "log","cog"]))