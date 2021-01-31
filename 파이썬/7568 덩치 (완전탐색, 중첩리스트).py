N = int(input())

people_list = []
for _ in range(N):
    temp = list(map(int, input().split()))
    people_list.append(temp)

for i in range(len(people_list)):
    cnt = 1
    myCnt = 1
    for j in range(len(people_list)):

        if i == j:
            continue
        elif people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            myCnt += 1

    print(myCnt, end=" ")
