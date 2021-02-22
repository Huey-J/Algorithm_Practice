def solution(n):
    cnt = 1
    answer = 0
    while n > 0:
        n -= 1
        temp = n % 3
        if temp == 0:
            temp = 1
        elif temp == 1:
            temp = 2
        else:
            temp = 4

        answer += temp * cnt
        cnt *= 10
        n = n // 3
    return str(answer)


print(solution(4))  # 출력용
