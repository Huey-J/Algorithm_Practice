memo = [0, 1, 1, 1, 2, 2] + [0] * (101 - 6)

for i in range(6, 101):
    memo[i] = memo[i-1] + memo[i-5]

N = int(input())
for _ in range(N):
    numb = int(input())
    print(memo[numb])
