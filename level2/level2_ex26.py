#(26) 캐시

def solution(cacheSize, cities):
    answer = 0
    result = []
    ciites = [x.lower() for x in cities]
    if cacheSize == 0:
        answer = len(cities)*5
        return answer
    for i in range(len(cities)):
        if len(result) < cacheSize:
            if cities[i] in result:
                answer += 1
                result.remove(cities[i])
            else:
                answer += 5
            result.append(cities[i])
        elif len(result) == cacheSize:
            if cities[i] in result:
                answer += 1
                result.remove(cities[i])
            else:
                result.pop(0)
                answer += 5
            result.append(cities[i])
        else:
            result.pop(0)
            result.append(cities[i])
            answer += 5
    return answer