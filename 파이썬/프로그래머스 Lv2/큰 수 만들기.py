from itertools import combinations


def solution(number, k):
    number_list = list(combinations(number, len(number)-k))

    tmp_list = []
    for n in number_list:
        tmp = ""
        for c in n:
            tmp += c
        tmp_list.append(int(tmp))
    return str(max(tmp_list))


print(solution("1924", 2))
