def solution(progresses, speeds):
    answer = []
    cnt = 0
    while 0 < len(progresses):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if len(progresses) == 0:
                break
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
    return answer


progresses, speeds = [93, 30, 55], [1, 30, 5]
print(solution(progresses, speeds))