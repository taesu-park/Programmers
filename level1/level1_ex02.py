#(2) 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    l = len(board)
    for m in moves:
        for i in range(l):
            if board[i][m-1] != 0:
                if stack and stack[-1] == board[i][m-1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer*2