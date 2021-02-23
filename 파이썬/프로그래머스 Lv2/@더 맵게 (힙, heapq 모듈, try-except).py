#### 내 답안1 (sort()함수에 의한 효율성 오류)
# def solution(scoville, K):
#     answer = 0
#     while True:
#         scoville.sort()
#         if scoville[0] < K and len(scoville) > 1:
#             answer += 1
#             min0 = scoville.pop(0)
#             min1 = scoville.pop(0)
#             scoville.append(min0 + min1 * 2)
#         else:
#             break
#
#     # 검사
#     for n in scoville:
#         if n < K:
#             return -1
#     return answer


#### 내 답안2 (heapq 모듈 활용하여 효율 up)
# sort()는 리스트 전체를 정렬하지만 heappush()는 현재 넣는 값만 올바르게 정렬하여 넣기 때문에 효율성이 더 좋다.
def solution(scoville, K):
    import heapq as hq
    answer = 0
    hq.heapify(scoville)  # 힙화 (정렬)
    while scoville[0] < K:
        try:
            answer += 1
            min0 = hq.heappop(scoville)
            min1 = hq.heappop(scoville)
            hq.heappush(scoville, min0 + min1 * 2)
        except IndexError:
            return -1
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
