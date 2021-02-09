'''
def makeOne(N):
    i = 0
    dp = []
    while True:
        if i == 0:
            if N % 6 == 0:
                dp.append([int(N / 3), int(N / 2), N - 1])
            elif N % 3 == 0:
                dp.append([int(N / 3), int(N - 1)])
            elif N % 2 == 0:
                dp.append([int(N / 2), N - 1])
            else:
                dp.append([N - 1])
        else:
            temp = []
            for k in dp[i - 1]:
                if k == 1:
                    return i

                if k % 6 == 0:
                    temp.append(int(k / 3))
                    temp.append(int(k / 2))
                    temp.append(k - 1)
                elif k % 3 == 0:
                    temp.append(int(k / 3))
                    temp.append(int(k - 1))
                elif k % 2 == 0:
                    temp.append(int(k / 2))
                    temp.append(k - 1)
                else:
                    temp.append(k - 1)
            temp = list(set(temp))
            dp.append(temp)
        i += 1


N = int(input())
print(makeOne(N))
'''

# 위 코드는 메모리 초과 오류
# 점화식: List[N] = min(List[N/3], List[N/2], list[N-1]) + 1
#       현재 단계  =     (이전 단계들 중 가장 작은값)         + 1

N = int(input())
result = [0 for _ in range(N + 1)]  # n+1개의 리스트 선언 result[i] = i값이 1이 되기 위한 최소 계산 개수
for i in range(2, N + 1):
    result[i] = result[i - 1] + 1                       # List[N] = List[N-1]
    if i % 3 == 0 and result[i // 3] + 1 < result[i]:   # 3으로 나뉘고 List[N//3]보다 작으면 List[N] = List[N//3]
        result[i] = result[i // 3] + 1
    if i % 2 == 0 and result[i // 2] + 1 < result[i]:   # 2로 나뉘고 List[N//2]보다 작으면 List[N] = List[N//2]
        result[i] = result[i // 2] + 1

print(result[N])
