def solution_wrong(s, skip, index):
    # skip 문자열 숫자화
    skip_list = []
    for c in skip:
        skip_list.append(ord(c))

    # skip_list.sort()

    answer = ''
    for c in s:
        c_number = ord(c)

        skip_count = 0
        for skip_number in skip_list:
            if c_number < skip_number < c_number + index:
                skip_count += 1
            # if c_number + index < skip_number:
            #     break

        result_number = c_number + index + skip_count

        answer += chr(result_number if result_number < ord('z') else result_number - 26)
    return answer


def solution(s, skip, index):
    # 유효한 알파벳 리스트 생성
    valid_chars = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]

    result = []

    for char in s:
        # 현재 문자의 유효한 알파벳 리스트에서의 인덱스
        current_index = valid_chars.index(char)
        # 이동한 후의 인덱스 계산
        new_index = (current_index + index) % len(valid_chars)
        # 새로운 문자 추가
        result.append(valid_chars[new_index])

    return ''.join(result)


print(solution("aukks", "wbqd", 5))     # happy 출력
