def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        cnt = 0
        for i in range(1, number + 1):
            if number % i == 0:
                cnt += 1
        
        if cnt % 2 == 0:
            answer += number
        else:
            answer -= number
    return answer


print(solution(13, 17))