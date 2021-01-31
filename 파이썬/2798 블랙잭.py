N, M = map(int, input().split())

num_list = list(map(int, input().split()))
num_list = num_list[0:N]  # 더 입력했을 경우 예외처리

max = 0
for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        for z in range(j + 1, len(num_list)):
            sum = num_list[i] + num_list[j] + num_list[z]
            if M >= sum > max:
                max = sum
print(max)
