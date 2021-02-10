'''
n = int(input())
dp = [[], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(1, n):
    tempList = []
    for j in dp[i]:
        number = j % 10
        if number == 0:
            tempList.append(j * 10 + (number + 1))
        elif number == 9:
            tempList.append(j * 10 + (number - 1))
        else:
            tempList.append(j * 10 + (number + 1))
            tempList.append(j * 10 + (number - 1))
    tempList = list(set(tempList))
    dp.append(tempList)

print(len(dp[n]) % 1000000000)
'''

# 위 코드는 DP[N]에 N자리수의 계단수를 넣었지만 메모리 초과 오류 ex) DP[1] = [1,2,3,4,5,6,7,8,9] (N=1의 계단수)
# 아래 코드에서는 DP[N]에 인덱스 기준 N자리수의 해당하는 숫자를 넣었다. ex) DP[1] = [0,1,1,1,1,1,1,1,1,1] (1의자리)

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(101)]  # = [[0] * 10] * 101]
for i in range(1, n + 1):
    for j in range(10):
        if i == 1:
            if j == 0: continue
            dp[i][j] = 1
        else:
            if j == 0:
                dp[i][j] += dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)
