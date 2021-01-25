'''
# 시간 초과 오류
# 문제 입력 조건에  1 <= n <= 123,456 이 있으므로
# 입력할 때 마다 소수를 계산하는 것은 비효율적이다.
# -> 미리 입력 조건에 해당하는 소수 리스트를 구해놓자.

while True:
    n = int(input())
    if n == 0: break

    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if i == 1: continue

        flag = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            cnt += 1
    print(cnt)
'''

num_list = []  # 소수 리스트 (1 <= n <= 123456)
# 소수 구하기
for i in range(1, 2 * 123456 + 1):
    if i == 1: continue
    flag = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0: num_list.append(i)

while True:
    n = int(input())
    if n == 0: break
    cnt = 0
    for i in num_list:
        if i > 2 * n: break
        if i > n: cnt += 1
    print(cnt)
