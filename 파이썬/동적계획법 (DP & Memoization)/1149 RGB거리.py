houses = []
N = int(input())
for _ in range(N):
    houses.append(list(map(int, input().split())))  # 이중 리스트 입력

for i in range(1, len(houses)):  # 이전과 비교하면서 리스트에 계속 더해감
    houses[i][0] += min(houses[i - 1][1], houses[i - 1][2])  # R선택
    houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])  # G선택
    houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])  # B선택
print(min(houses[N - 1][0], houses[N - 1][1], houses[N - 1][2]))
