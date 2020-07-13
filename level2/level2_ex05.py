#(5) 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        result = ''
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                result += skill_trees[i][j]
        if not result:
            answer += 1
        else:
            for s in range(len(result)):
                if result[s] == skill[s]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                answer += 1

    return answer