def solution(priorities, location):
    printer = []
    for i in range(len(priorities)):
        if i == location:
            printer.append((priorities[i], True))       # location에 True 표시
        else:
            printer.append((priorities[i], False))

    answer = 0
    while True:
        now = printer.pop(0)
        # print(answer, now, printer)
        for i in range(0, len(printer)):
            if now[0] < printer[i][0]:      # 현재 보다 큰 값이 있으므로 뒤에 다시 추가
                printer.append(now)
                break
        else:                       # Break 되지 않았으므로 pop처리
            answer += 1
            if now[1]:              # True 표시 되어 있으면 반환
                return answer


print(solution([2, 3, 2, 2], 0))


#### 내 답안 (location 이동)
#### 모범답안 (튜플 이용)
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]     # (index, value)의 튜플 리스트 생성
#     answer = 0
#     while True:
#         cur = queue.pop(0)            # 첫번째 값 pop() 후 값 저장
#         if any(cur[1] < q[1] for q in queue):     # 값이 큰게 있다면 append()
#             queue.append(cur)
#         else:
#             answer += 1           # pop() 값이 제일 크면 answer+=1
#             if cur[0] == location:    # location과 index가 같으면 반환!
#                 return answer
