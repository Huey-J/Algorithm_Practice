def solution(n):
    answer = 0
    list = []
    for i in range(1, n):
        list.append(i)
        while sum(list) > n:
            list.pop(0)
        if sum(list) == n:
            answer += 1
    return answer + 1


print(solution(15))