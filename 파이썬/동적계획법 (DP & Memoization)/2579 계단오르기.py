n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [stairs[0]]    # 첫 번째 계단
for i in range(1, n):
    if i == 1:      # 두 번째 계단
        dp.append(max(dp[0] + stairs[1], stairs[1]))  # 0 + 1 vs 1
    elif i == 2:    # 세 번째 계단
        dp.append(max(dp[0] + stairs[2], stairs[1] + stairs[2]))  # 0 + 2 vs 1까지의 합 + 현재 계단
    else:
        dp.append(max(dp[i - 2] + stairs[i],                    # i-2까지의 합 + 현재 계단
                      dp[i - 3] + stairs[i - 1] + stairs[i]))   # i-3까지의 합 + i-1계단 + 현재 계단

print(dp[-1])

# 인덱스는 +1 or +2 (최대값)
# 마지막계단 n의 이전은 n-1 or n-2
# 마지막 계단을 밟아야 함 (뒤를 기준으로 계산)
