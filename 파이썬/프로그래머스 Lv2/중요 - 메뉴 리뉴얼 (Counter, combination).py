from itertools import combinations
from collections import Counter
def solution(orders, course):
    course_list = []
    for number in course:           # 코스요리 숫자로 반복
        combination_list = []
        for order in orders:
            tmp_list = list(combinations(order, number))
            for t in tmp_list:
                print(t, sorted(t))
                combination_list.append(''.join(sorted(t)))     # sorted로 AB, BA를 같은 음식으로 인식하도록 함
        # print(combination_list, end="\n\n")

        # 사전으로 정의, count의 내림차순으로 정렬
        combination_dict = sorted(dict(Counter(combination_list)).items(), key=lambda x: x[1], reverse=True)

        # 가장 많이 count된 내용 추가 (중복)
        # 중복 없으면 Counter().most_common(1) 사용
        for i in range(len(combination_dict)):
            if combination_dict[i][1] < 2:
                break
            if combination_dict[i][1] != combination_dict[0][1]:
                break
            course_list.append(combination_dict[i][0])

    return sorted(course_list)


print(solution(
    ["XYZ", "XWY", "WXA"], [2, 3, 4]
))