#### 내 답안1 (순열 이용하면 시간 초과 오류)
# def solution(numbers):
#     from itertools import permutations
#
#     # 숫자 조합 만들기 (순열)
#     per_list = permutations(numbers)
#     num_list = []
#     for t in per_list:
#         num_list.append(int("".join(map(str, t))))
#     # print(num_list)
#     return str(max(num_list))


def solution(num):
    num = list(map(str, num))       # string list로 변환
    num.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(num)))

# lambda x : x*3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다.
# x*3을 하는 이유? -> num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.

# 문자열 비교는 ASCII 값으로 치환되어 정렬된다. 따라서 666, 101010, 222의 첫번째 인덱스 값으로 비교한다.
# 6 = 86, 1 = 81, 2 = 82 이므로 6 > 2 > 1순으로 크다.
# 이를 reverse = True를 통해 내림차순 해주면 6,2,10이 된다. 이것을 ''.join(num)을 통해 문자열을 합쳐주면 된다.

# 모든 값이 0일 때(즉, '000'을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.

print(solution([6, 10, 2]))
