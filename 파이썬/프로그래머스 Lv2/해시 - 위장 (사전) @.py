# # Counter 사용
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     return reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1


# # 정석 풀이 : 해시, 사전 사용
# def solution(clothes):
#     clothes_type = {}

#     for c, t in clothes:
#         print(clothes_type)
#         if t not in clothes_type:
#             clothes_type[t] = 2       # 해당 종류의 의상이 없을 때 그 의상을 더 해주면서 아무것도 안입었을 때의 경우를 함께 생각해서 2를 더해줌
#         else:
#             clothes_type[t] += 1
#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num

#     return cnt - 1                    # 아무것도 안쓰는 경우를 제외


# 내 답안
def solution(clothes):
    select_list = []  # 0번째 인덱스가 의류 타입인 리스트들의 리스트
    for c in clothes:
        for s in select_list:
            if s[0] == c[1]:
                s.append(c[0])
                break
        else:
            select_list.append([c[1], c[0]])
    # print(select_list)
    answer = 1
    for s in select_list:   # 타입별로 개수+1만큼씩 곱함
        answer *= len(s)

    return answer - 1       # 아무것도 안쓰는 경우를 제외


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
