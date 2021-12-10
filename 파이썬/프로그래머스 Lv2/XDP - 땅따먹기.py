def solution(land):
    for i in range(0, len(land)-1):
        # print(land)
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i+1][3] += max(land[i][0], land[i][1], land[i][2])
    # print(land)
    return max(land[len(land)-1])


print(solution([[1,2,3,4,3],[3,2,1,9],[5,3,2,7]]))


### 오답 : 재귀함수로 모든 경우의 수 구함
# def recursive(before_index, rest_land, total, answer_list):
#     print(before_index, rest_land, total)
#     if len(rest_land) < 1:
#         answer_list.append(total)
#         # print(">>>>>total:", total)
#         return total

#     for i in range(4):
#         if before_index != i:
#             recursive(i, rest_land[1:], total+rest_land[0][i], answer_list)


# def solution(land):
#     answer_list = []
#     for i in range(4):
#         recursive(i, land[1:], land[0][i], answer_list)
#     # print(answer_list)

#     return max(answer_list)