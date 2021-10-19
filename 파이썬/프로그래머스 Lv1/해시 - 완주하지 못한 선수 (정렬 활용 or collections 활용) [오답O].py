participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

#### 3. 정렬 이용
# participant.sort()
# completion.sort()
# for i in range(len(completion)):
#     # print(participant[i], completion[i])
#     if participant[i] != completion[i]:
#         print(participant[i])
#         break
# print(participant[-1])

#### 2. 버블정렬
# participant.sort()
# for temp_completion in completion:
#     people = []
#     people += participant
#     while True:
#         mid = len(people) // 2
#         if temp_completion < people[mid]:
#             people = people[:mid]
#         elif temp_completion > people[mid]:
#             people = people[mid:]
#         else:
#             participant.remove(temp_completion)
#             break
# answer = participant.pop()
# print(answer)

#### 1. 하나씩
# for _ in range(len(completion)):
#     participant.remove(completion.pop())
# answer = participant.pop()
# print(answer)


#### 내 답안
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return(participant[-1])

#### 모범 답안 (라이브러리 활용)
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]

print(solution(participant, completion))