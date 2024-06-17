def solution_wrong(ingredient):
    count = 0
    i = 0
    while 1:
        if ingredient[i: i + 4] == [1, 2, 3, 1]:
            ingredient = ingredient[:i] + ingredient[i + 3:]
            count += 1
            i = i - 4 if i > 4 else 0
        i += 1
        if i >= len(ingredient):
            break

    return count


def solution(ingredient):
    stack = []
    count = 0

    # 패턴은 [1, 2, 3, 1]
    pattern = [1, 2, 3, 1]

    for item in ingredient:
        stack.append(item)

        # 스택의 마지막 4개 요소가 패턴과 일치하는지 확인
        if len(stack) >= 4 and stack[-4:] == pattern:
            count += 1
            # 패턴을 제거
            del stack[-4:]

    return count


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))  # 출력: 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))  # 출력: 0
