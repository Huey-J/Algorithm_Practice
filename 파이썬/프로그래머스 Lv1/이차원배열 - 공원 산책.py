def solution(park, routes):
    # Action 정의
    action_dict = {
        'E': [0, 1],
        'W': [0, -1],
        'S': [1, 0],
        'N': [-1, 0]
    }

    # park 크기 정의
    park_size = [len(park), len(park[0])]

    # 현재 위치 정의
    now_position = [0, 0]
    for i in range(0, len(park)):
        for j in range(0, len(park[0])):
            if park[i][j] == 'S':
                now_position = [i, j]

    print("Start Position", now_position)

    for route in routes:
        # Action 구하기
        action = [action_dict[route[0]][0] * int(route[2]), action_dict[route[0]][1] * int(route[2])]
        action_result = [now_position[0] + action[0], now_position[1] + action[1]]

        # park 범위 벗어나는지 확인
        if action_result[0] < 0 or park_size[0] <= action_result[0] or action_result[1] < 0 or park_size[1] <= action_result[1]:
            print("Pass: out of the park")
            continue

        # 장애물 있는지 확인
        flag = 0
        if action[0] + action[1] > 0:
            for i in range(now_position[0], action_result[0] + 1):
                if park[i][now_position[1]] == 'X':
                    print("장애물 position 0")
                    flag = 1
                    break
            for j in range(now_position[1], action_result[1] + 1):
                if park[now_position[0]][j] == 'X':
                    print("장애물 position 1")
                    flag = 1
                    break
        else:
            for i in range(action_result[0], now_position[0]):
                if park[i][now_position[1]] == 'X':
                    print("장애물 position 0")
                    flag = 1
                    break
            for j in range(action_result[1], now_position[1]):
                if park[now_position[0]][j] == 'X':
                    print("장애물 position 1")
                    flag = 1
                    break
        if flag == 1:
            continue

        # Action 반영
        now_position = action_result
        print(now_position)
    return now_position


# print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
# print('--------')
# print(solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))
# print('--------')
# print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
print('--------')
print(solution(["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"]))    # [1, 1]
# print('--------')
# print(solution(["SXO", "OXX", "OOO"], ["E 4", "S 4", "N 4", "S 1", "S 1", "E 2"]))  # [2, 2]

