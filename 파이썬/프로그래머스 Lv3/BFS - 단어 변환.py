# 모범 답안 : 재귀함수 활용 (DFS방식) (BFS방식이 올바름)
# answer = 0
# def solution(begin, target, words):
#     dfs(begin, target, 0, words)
#     return answer

# def change(fr, to):
#     for i in range(len(fr)):
#         if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]:
#             return True
#     return False

# def dfs(begin, target, d, words):
#     global answer
#     # print(begin, target, d, words)
#     if begin == target:
#         answer = d
#         return
#     else:
#         if len(words) == 0:
#             return 
#         for w in range(len(words)):
#             if change(begin, words[w]):
#                 word = words[:w]+words[w+1:]
#                 dfs(words[w], target, d+1, word)




# # 내 답안 : while문 활용 (BFS방식)
# def find_possible_word(str1, str2, length):
#     cnt = 0
#     for i in range(length):
#         if str1[i] != str2[i]:
#             cnt += 1
#     # 다른 문자가 하나만 있는 경우 True 반환
#     if cnt == 1:
#         return True
#     else:
#         return False


# def solution(begin, target, words):
#     if words.count(target) == 0:
#         return 0

#     nows = [begin]
#     time = 0
#     length = len(begin)
#     while True:
#         print(time, nows)

#         if len(words) == 0:     # 탈출 조건 1 : 끝까지 담았지만 못 찾을 경우
#             return 0
#         for now in nows:        # 탈출 조건 2 : target을 완성한 경우
#             if now == target:
#                 return time

#         tmp_nows_wrapper = []
#         for i in range(len(nows)):
#             tmp_nows = []
#             for j in range(len(words)):
#                 if find_possible_word(nows[i], words[j], length):
#                     tmp_nows.append(words[j])
#             tmp_nows_wrapper += tmp_nows
#         nows = tmp_nows_wrapper
#         time += 1


print("return", solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
