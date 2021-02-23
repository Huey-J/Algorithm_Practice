n = int(input())
num_list = []
for _ in range(n):
    a, b = map(int, input().split())
    num_list.append([a, b])

# 시작시간으로 오름차순 정렬
num_list.sort(key=lambda temp: temp[0])
# 종료시간으로 오름차순 정렬
num_list.sort(key=lambda temp: temp[1])

# 첫번째 예약은 무조건 넣고 끝나는 시간을 저장
now_end = num_list[0][1]
cnt = 1
for i in range(1, n):
    if now_end <= num_list[i][0]:
        now_end = num_list[i][1]
        cnt += 1

print(cnt)
