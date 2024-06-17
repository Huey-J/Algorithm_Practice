def solution(name_list, yearnings_list, photo_list):
    # dictionary 생성
    yearning_dictionary = dict()
    for i in range(0, len(name_list)):
        yearning_dictionary[name_list[i]] = yearnings_list[i]

    # 그리움 지수 구하기
    answer_list = []
    for photo in photo_list:
        answer = 0
        for name in photo:
            answer += yearning_dictionary.get(name) if yearning_dictionary.get(name) is not None else 0
        answer_list.append(answer)

    return answer_list


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
