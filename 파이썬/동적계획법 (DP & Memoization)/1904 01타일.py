n = int(input())
memo = [0, 1, 2] + [0] * (1000001 - 3)  #선언

for i in range(3, n + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

print(memo[n])
