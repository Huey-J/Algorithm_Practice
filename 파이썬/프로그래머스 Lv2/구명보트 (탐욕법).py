def solution(people, limit):
    answer = len(people)
    people.sort()
    start = 0
    end = len(people)-1
    while start < end: # 두명씩 탑승
        if people[start] + people[end] <= limit:
            answer -= 1
            start += 1
        end -= 1
    return answer


print(solution([70, 80, 50], 100))
