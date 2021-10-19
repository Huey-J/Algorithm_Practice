def solution(board, moves):
    result = 0
    x = len(board[0])
    y = len(board)

    stack = []
    for move in moves:                                 # 움직임 처리
        for i in range(y):                             # 아래로 내려감
            if board[i][move-1] != 0:                  # 값이 나오면
                stack.append(board[i][move-1])         # 스택에 넣고
                board[i][move-1] = 0                   # 0으로 비움 처리

                if len(stack) > 1:                     # stack에 쌓인 값이 2개 이상이면
                    if stack[-1] == stack[-2]:         # 최근 두개 값 비교해서 같으면 boom!
                        result += 2
                        stack.pop()
                        stack.pop()
                break
    
    return result


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))