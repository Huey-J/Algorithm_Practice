def 약수개수(number):
    count = 0
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            count += 1
            if i != number // i:
                count += 1  # n // i is a divisor different from i
    return count


def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        count = 약수개수(num)
        answer += count if count <= limit else power

    return answer


print(solution(5, 3, 2))  # 10 출력
print(solution(10, 3, 2))  # 21 출력
