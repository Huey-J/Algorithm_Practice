def recursion(numbers, target, sum):
    temp = [] + numbers
    if len(temp) < 1:
        # print(numbers, target, sum)
        if target == sum:
            return 1
        else:
            return 0
    else:
        n = temp.pop()
        return recursion(temp, target, sum + n) + recursion(temp, target, sum - n)


def solution(numbers, target):
    return recursion(numbers, target, 0)


print(solution([1, 1, 1, 1, 1], 3))
