def solution(numbers, hand):
    answer = ''
    l_position, r_position = '*','#'
    left, right, center= ['1','4','7','*'],['3','6','9','#'],['2','5','8','0']
    l_index, r_index = 3, 3
    for i in range(len(numbers)):
        print(l_position,r_position,answer)
        if str(numbers[i]) in left:
            answer += 'L'
            l_position = str(numbers[i])
            l_index = left.index(str(numbers[i]))
        elif str(numbers[i]) in right:
            answer += 'R'
            r_position = str(numbers[i])
            r_index = right.index(str(numbers[i]))
        else:
            if l_position in center:
                r_index += 1
            elif r_position in center:
                l_index += 1
            if abs(center.index(str(numbers[i])) - l_index)> abs(center.index(str(numbers[i])) - r_index):
                answer += 'R'
                r_position = str(numbers[i])
                r_index = center.index(str(numbers[i]))
            elif abs(center.index(str(numbers[i])) - l_index) < abs(center.index(str(numbers[i])) - r_index):
                answer += 'L'
                l_position = str(numbers[i])
                l_index = center.index(str(numbers[i]))
            else:
                if hand == 'right':
                    answer += 'R'
                    r_position = str(numbers[i])
                    r_index = center.index(str(numbers[i]))
                else:
                    answer += 'L'
                    l_position = str(numbers[i])
                    l_index = center.index(str(numbers[i]))
                    


    return answer
solution(
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
"right")