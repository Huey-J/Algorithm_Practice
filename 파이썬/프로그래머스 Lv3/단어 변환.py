# def solution(begin, target, words):
#     if target not in words:  # words에 target이 없을 경우
#         return 0
#
#     answer = 0
#     dfs = []  # DFS를 위한 스택
#     words_length = len(words)
#     visited = [0] * words_length  # 방문한 노드는 1 / 방문 안한 노드는 0
#     str_length = len(begin)
#
#     while 0 in visited:  # 방문 안한 노드가 있으면 반복
#         if answer != 0:
#             dfs.append(visited.index(0))  # 방문 안한(0) 노드를 찾아 DFS 스택에 넣음
#         while dfs or answer == 0:
#             if answer != 0:
#                 node = dfs.pop(-1)
#                 visited[node] = 1
#                 tmp_str = words[node]
#             else:
#                 tmp_str = begin
#             print(dfs)
#             for i in range(words_length):
#                 if visited[i] == 0:
#                     print(1)
#                     cnt = 0
#                     for j in range(str_length):
#                         if words[i][j] != tmp_str[j]:
#                             cnt += 1
#                     if cnt == 1:
#                         dfs.append(j)
#         print(dfs)
#     return answer

def solution(begin, target, words):
    answer = 0
    queue = [begin]
    while True:
        tmp_q = []
        for word_1 in queue:
            if word_1 == target:
                return answer
            for word_2_idx in range(len(words)-1, -1, -1):
                word_2 = words[word_2_idx]
                difference = sum([x != y for x, y in zip(word_1, word_2)])
                if difference == 1:
                    tmp_q.append(words.pop(word_2_idx))
        if not tmp_q:
            return 0
        queue = tmp_q
        answer += 1

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
