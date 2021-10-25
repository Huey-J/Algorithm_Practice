def solution(n,a,b):
    arr = []
    for i in range(n):
        arr.append([i + 1])

    answer = 1
    while n > 1:
        tmp = []
        i = 0
        while i < len(arr):
            tmp.append(arr[i] + arr[i+1])
            i += 2
        for t in tmp:
            if a in t and b in t:
                return answer
        arr = tmp
        n //= 2
        answer += 1
    return answer

# 모범 답안
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2
    # return answer


print(solution(8,4,7))