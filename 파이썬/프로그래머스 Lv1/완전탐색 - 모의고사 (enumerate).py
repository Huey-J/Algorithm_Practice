def solution(input):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    cnt = [0, 0, 0]

    for i in range(len(input)):
        if p1[i%5] == input[i]:
            cnt[0] += 1
        if p2[i%8] == input[i]:
            cnt[1] += 1
        if p3[i%10] == input[i]:
            cnt[2] += 1
    
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    return answer


input = list(map(int, input().split()))
print(solution(input))


# enumerate 함수 사용
# def another_solution(answer):
#     for i, answer in enumerate(answers):
#         if answer = p1[i % len(p1)]:
#             cnt[0] += 1
