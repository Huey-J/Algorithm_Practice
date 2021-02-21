board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

answer = 0  # 사라진 인형의 개수
bucket = []  # 바구니

for temp in moves:
    for i in range(len(board)):
        if board[i][temp - 1] != 0:
            bucket.append(board[i][temp - 1])  # 바구니에 넣기
            if len(bucket) > 1:  # 바구니 검사
                if bucket[-1] == bucket[-2]:
                    bucket.pop()
                    bucket.pop()
                    answer += 2

            board[i][temp - 1] = 0  # 인형 비우기
            break
print(answer)



# def solution(board, moves):
#     answer = 0  # 사라진 인형의 개수
#     bucket = []  # 바구니
#
#     for temp in moves:
#         for i in range(len(board)):
#             if board[i][temp - 1] != 0:
#                 bucket.append(board[i][temp - 1])  # 바구니에 넣기
#                 if len(bucket) > 1:  # 바구니 검사
#                     if bucket[-1] == bucket[-2]:
#                         bucket.pop()
#                         bucket.pop()
#                         answer += 2
#
#                 board[i][temp - 1] = 0  # 인형 비우기
#                 break
#     return answer
