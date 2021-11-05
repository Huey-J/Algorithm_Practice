def solution(n, computers):
    answer = 0
    bfs = []  # BFS를 위한 리스트(큐)
    visited = [0] * n  # 방문한 노드는 1 / 방문 안한 노드는 0

    while 0 in visited:  # 방문 안한 노드가 있으면 반복
        bfs.append(visited.index(0))  # 방문 안한(0) 노드를 찾아 BFS 큐에 넣음
        while bfs:  # BFS 큐 실행
            node = bfs.pop(0)  # 최근에 넣은 노드 추출

            visited[node] = 1  # 하나씩 방문시키기
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:  # 아직 방문 안한 노드이고 연결되어 있다면 큐에 넣음
                    bfs.append(i)
        answer += 1  # 해당 노드의 BFS가 끝나면 네트워크 1개 탐색 완료
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
