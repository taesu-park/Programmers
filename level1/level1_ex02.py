import pprint

def solution(board, moves):
    answer = 0
    stack = []
    l = len(board)
    for m in moves:
        pprint.pprint(board)
        print(stack)
        for i in range(l):
            if board[i][m-1] != 0:
                if stack and stack[-1] == board[i][m-1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],[1, 5, 3, 5, 1, 2, 1, 4])