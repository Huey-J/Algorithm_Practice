# 모범 답안 : 스택 활용
def solution(number, k):
    collected = []  # 숫자를 모아서 큰 수를 만들 때 쓰일 배열
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)
    return answer



# # 오답 2 : Slice 이용 (두개 시간 초과)
# def find_max_index(value):
#     maximum = -1
#     answer = 0
#     for i in range(len(value)):
#         if int(value[i]) > maximum:
#             maximum = int(value[i])
#             answer = i
#     return answer

# def solution(number, k):
#     answer = ""
#     k = len(number) - k
#     while k > 0:
#         endIndex = len(number) - k      # 끝 값 설정

#         # 그리디
#         maxIndex = find_max_index(number[:endIndex+1])
#         answer += number[maxIndex]
#         number = number[maxIndex+1:]
#         k -= 1
#     return answer


# # 오답 1 : 조합 이용 (제한시간 오류)
# from itertools import combinations

# def solution(number, k):
#     number_list = list(combinations(number, len(number)-k))
#     tmp_list = []
#     for n in number_list:
#         tmp = ""
#         for c in n:
#             tmp += c
#         tmp_list.append(int(tmp))
#     return str(max(tmp_list))


print(solution("4177252841", 4))
