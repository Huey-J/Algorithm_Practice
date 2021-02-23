from itertools import permutations


def solution(numbers):
    num_list = list(n for n in numbers)  # 중복 제거된 숫자 리스트

    # 숫자 조합 만들기 (순열)
    per_list = []
    for i in range(1, len(numbers) + 1):
        tmp_list = list(permutations(num_list, i))  # 조합 리스트
        for t in tmp_list:
            per_list.append(int("".join(t)))  # join으로 묶고 int형 변환
    per_list = list(set(per_list))  # 중복 제거

    # 소수 개수 count
    # print(per_list)
    answer = 0
    for n in per_list:
        if n == 0 or n == 1:
            continue
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(n, i)
                break
        else:
            answer += 1
    return answer


print(solution("011"))

# 필요한 소수 리스트 만들기
# sosu_list = []
# for n in range(3, 10 ** len(numbers)):  # numbers 개수만큼 소수 구하기
#     for i in range(2, int(n ** 0.5) + 1):  # 제곱근 까지만 비교
#         if n % i == 0:
#             break
#     else:
#         sosu_list.append(n)
