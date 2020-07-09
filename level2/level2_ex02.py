#(2) 구명보트

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l_index, r_index = -1,len(people)-1
    while l_index != r_index:
        l_index += 1
        if people[l_index] + people[r_index] <= limit and l_index != r_index:
            r_index -= 1
        answer += 1
    return answer
