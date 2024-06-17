def solution(t, p):
    t_length = len(t)
    p_length = len(p)

    # 1. 숫자 리스트 추출
    str_list = []
    for i in range(0, t_length - p_length + 1):
        str_list.append(t[i:i + p_length])

    # 2. 비교
    answer = 0
    for str_number in str_list:
        answer += 1 if int(str_number) <= int(p) else 0

    return answer


print(solution("3141592", "271"))
