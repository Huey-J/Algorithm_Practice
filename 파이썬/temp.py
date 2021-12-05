from collections import Counter

def solution(arr):
    d = Counter(arr)
    
    for number in arr:
        print(number, d[number])

    # return next((x for x in arr if d[x] == 1), -1)


print(solution([1,2,1,3,3,2,5]))