M, N = map(int, input().split())
for i in range(M, N + 1):
    if i == 1:      # 1은 소수가 아니다.
        continue;

    flag = 0
    for j in range(2, int(i ** 0.5) + 1):   # 해당 숫자의 제곱근(루트)까지만 시도
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)
