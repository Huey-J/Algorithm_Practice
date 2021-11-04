def solution(bridge_length, weight, truck_weights):
    done_now, count_now, bridge_now = [], [], []
    done_length = len(truck_weights)
    time = 0
    while True:
        # 다 건너면 종료
        if len(done_now) == done_length:
            break
        
        # 건너는 중
        i = 0
        while len(count_now) > i:
            if count_now[i] == bridge_length:
                done_now.append(bridge_now.pop(i))
                count_now.pop(i)
                i = 0
            else:
                count_now[i] += 1
                i += 1
        
        # 다리에 올라갈 수 있으면 추가
        if len(truck_weights) != 0:
            if sum(bridge_now) + truck_weights[0] <= weight:
                bridge_now.append(truck_weights.pop(0))
                count_now.append(1)
        time += 1
        # print(time, done_now, bridge_now)
    return time



print("return", solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
