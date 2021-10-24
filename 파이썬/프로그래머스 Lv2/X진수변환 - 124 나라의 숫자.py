# 모범 답안
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3
    return answer

print(change124(13))






# def solution(n):
#     cnt = 1
#     answer = 0
#     while n > 0:
#         n -= 1
#         temp = n % 3
#         if temp == 0:
#             temp = 1
#         elif temp == 1:
#             temp = 2
#         else:
#             temp = 4

#         answer += temp * cnt
#         cnt *= 10
#         n = n // 3
#     return str(answer)


# print(solution(4))
