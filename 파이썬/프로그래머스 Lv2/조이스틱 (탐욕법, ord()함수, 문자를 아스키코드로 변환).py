def solution(name):
    # 이동하기 위한 조이스틱 작동 횟수 리스트
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    idx, answer = 0, 0

    while True:
        answer += make_name[idx]    # 알파벳 idx 완성
        make_name[idx] = 0          # idx는 더이상 이동할 필요 없음
        if sum(make_name) == 0:     # make_name이 모두 0이면 조작할게 남지 않은 것이므로 종료
            break

        # 근처 알파벳 까지 이동 거리 계산
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1

        # 이동 방향 정하기
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
            
    return answer


print(solution("JAZN"))
