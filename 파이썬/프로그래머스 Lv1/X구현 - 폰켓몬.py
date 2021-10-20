from itertools import combinations

def solution(nums):
    tmp = list(set(nums))
    
    answer = len(nums)//2
    if len(tmp) < answer:
        answer = len(tmp)
    return answer

# 모범 답안
# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))


nums = [1,3,1,1,1,2,6,6,6,6]
print(solution(nums))