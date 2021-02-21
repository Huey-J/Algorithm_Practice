answers = [1, 2, 3, 4, 5]

cnt1, cnt2, cnt3 = 0, 0, 0
p1 = [1, 2, 3, 4, 5]
p2 = [2, 1, 2, 3, 2, 4, 2, 5]
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
for i in range(len(answers)):
    if answers[i] == p1[i % len(p1)]:  # 사람1
        cnt1 += 1
    if answers[i] == p2[i % len(p2)]:  # 사람2
        cnt2 += 1
    if answers[i] == p3[i % len(p3)]:  # 사람3
        cnt3 += 1

p_list = [[1, cnt1], [2, cnt2], [3, cnt3]]
p_list.sort(key=lambda k: k[1], reverse=True)

answer = []
for i in range(3):
    if p_list[i][1] != p_list[0][1]:
        break
    answer.append(p_list[i][0])
print(answer)



#### 내 답안
# def solution(answers):
#     cnt1, cnt2, cnt3 = 0, 0, 0
#     p1 = [1, 2, 3, 4, 5]
#     p2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     for i in range(len(answers)):
#         if answers[i] == p1[i % len(p1)]:  # 사람1
#             cnt1 += 1
#         if answers[i] == p2[i % len(p2)]:  # 사람2
#             cnt2 += 1
#         if answers[i] == p3[i % len(p3)]:  # 사람3
#             cnt3 += 1
#
#     p_list = [[1, cnt1], [2, cnt2], [3, cnt3]]
#     p_list.sort(key=lambda k: k[1], reverse=True)
#     answer = []
#     for i in range(3):
#         if p_list[i][1] != p_list[0][1]:
#             break
#         answer.append(p_list[i][0])
#
#     return answer
