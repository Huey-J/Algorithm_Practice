def solution(a, b, n):
    answer = 0
    while a <= n:
        count = (n // a) * b
        n = count + n % a
        answer += count

    return answer


print(solution(2, 1, 20))  # -> 19

# 20개 가져다 주면 10개
# 10개 가져다 주면 5개
# 5개 가져다 주면 2개
# 2개 가져다 주면 1개
