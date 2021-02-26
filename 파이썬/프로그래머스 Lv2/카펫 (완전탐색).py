def solution(brown, yellow):
    # 합친 값의 약수 구하기
    sum = brown + yellow
    list = []
    for i in range(1, sum + 1):
        if sum % i == 0:
            list.append(i)

    # 조합 찾기
    for i in range(len(list)):
        j = len(list) - i - 1
        if i > j:  # 탈출조건
            break

        print(list[i], list[j])
        if (list[i] - 2) * (list[j] - 2) == yellow:
            return [list[j], list[i]]
    return []


print(solution(24, 24))
