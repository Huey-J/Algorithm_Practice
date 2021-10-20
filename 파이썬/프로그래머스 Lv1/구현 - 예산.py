def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    for now in d:
        if now + sum <= budget:
            answer += 1
            sum += now
        else:
            break
    return answer