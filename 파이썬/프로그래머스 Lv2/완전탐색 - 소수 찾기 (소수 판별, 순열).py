from itertools import permutations


def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    # 순열 활용
    number_list = []
    for i in range(1, len(numbers)+1):
        permutations_list = list(permutations(numbers, i))
        for comb in permutations_list:
            number_list.append(int("".join(comb)))
    
    # 중복 숫자 제거
    number_list = list(set(number_list))

    # 소수 개수
    answer = 0
    for num in number_list:
        if is_prime_number(num):
            answer += 1
    return answer


print(solution("17"))
