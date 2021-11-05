# 내 풀이 : 약수로 가능한 가로x세로 리스트 구해서 둘레 활용
def get_number(number):              # 약수 리스트
    result = []
    for i in range(3, number//2):    # 1, 2는 yellow를 감쌀 수 없으므로 제외
        if number % i == 0:
            result.append(i)
    return sorted(list(result))


def solution(brown, yellow):
    number_list = get_number(brown + yellow)
    for i in range(len(number_list)//2 + 1):
        if 2 * number_list[-i-1] + (number_list[i] - 2) * 2 == brown:                   # brown은 둘레의 길이와 같음
            return [number_list[-i-1], number_list[i]]

        # 위 if문을 정석으로 하면
        # 둘레의 길이 = 가로*2 + 세로*2 - 4(겹치는 부분)
        # brown = number_list[i]*2 + number_list[-i-1]*2 - 4

print(solution(24, 24))


# 예전 내 풀이
# def solution(brown, yellow):
#     # 합친 값의 약수 구하기
#     sum = brown + yellow
#     list = []
#     for i in range(1, sum + 1):
#         if sum % i == 0:
#             list.append(i)

#     # 조합 찾기
#     for i in range(len(list)):
#         j = len(list) - i - 1
#         if i > j:  # 탈출조건
#             break

#         print(list[i], list[j])
#         if (list[i] - 2) * (list[j] - 2) == yellow:
#             return [list[j], list[i]]
#     return []
