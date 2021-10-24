def solution(citations):
    maxValue = max(citations)
    result = 0
    for hIndex in range(maxValue):
        cnt = 0
        for val in citations:
            if hIndex <= val:
                cnt += 1
        if hIndex <= cnt:
            result = hIndex
    return result


citations = [3, 0, 6, 1, 5]
print(solution(citations))