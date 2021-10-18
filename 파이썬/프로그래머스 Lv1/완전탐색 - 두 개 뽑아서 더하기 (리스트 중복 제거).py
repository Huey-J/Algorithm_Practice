def solution(numbers):
    sum = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            sum.append(numbers[i] + numbers[j])
    return sorted(list(set(sum)))


inputs = list(map(int, input().split()))
print(solution(inputs))
