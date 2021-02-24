def solution(citations):
    for h in range(citations[0], -1, -1):
        bigger_cnt = 0
        smaller_cnt = 0
        for i in citations:
            if i >= h:
                bigger_cnt += 1
            if i <= h:
                smaller_cnt += 1
        if bigger_cnt >= h >= smaller_cnt:
            print(bigger_cnt, h, smaller_cnt)
            break
    return h


print(solution([3, 0, 6, 1, 5]))
