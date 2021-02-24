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
