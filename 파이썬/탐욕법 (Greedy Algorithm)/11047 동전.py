# 동전의 가치는 서로 배수관계라는 조건이 있기 때문에 탐욕법으로 최적의 답을 구할 수 있다.
n, k = map(int, input().split())
num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.reverse()
cnt = 0
while True:
    for temp in num_list:
        if temp <= k:
            # 최대한 나누고 남은 값으로 반복
            cnt += k // temp
            k %= temp
            break
    if k == 0:
        break
print(cnt)
