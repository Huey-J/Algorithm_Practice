def solution(priorities, location):
    answer = 0
    while True:
        k = priorities[0]
        for i in range(1, len(priorities)):
            if k < priorities[i]:
                priorities.append(priorities.pop(0))  # 뒤로 보내기
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1
                break
        # print(priorities, location, answer)
        if i == len(priorities) - 1:
            if location == 0:
                return answer + 1
            priorities.pop(0)
            location -= 1
            answer += 1
        if len(priorities) == 1:
            break

    return answer + 1


print(solution([2, 1, 3, 2], 2))


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
