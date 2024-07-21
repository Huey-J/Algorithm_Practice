def solution(s):
    answer = 0

    count_x = 0
    count_y = 0
    char_x = s[0]
    for c in s:
        if (count_x == 0):
            char_x = c

        if (char_x == c):
            count_x += 1
        else:
            count_y += 1

        if (count_x == count_y):
            answer += 1
            count_x = 0
            count_y = 0

    if (count_x != 0 or count_y != 0):
        answer += 1

    return answer


print(solution("banana"))       # 3
print(solution("abracadabra"))  # 6
