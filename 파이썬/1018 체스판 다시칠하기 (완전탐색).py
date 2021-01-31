def changeBuffer(tempBuffer):
    if tempBuffer == 'W':
        return 'B'
    else:
        return 'W'


N, M = map(int, input().split())
chessList = []
for _ in range(N):
    tempStr = input()
    chessList.append(tempStr)

min_cnt = M * N
for i in range(N - 7):
    for j in range(M - 7):
        buff = chessList[i][j]  # (i,j) = 8*8 시작점
        cnt = 0

        for t in range(i, i + 8):
            for k in range(j, j + 8):
                if k == j:
                    if t == i:  # 첫 번째는 비교할 대상이 없기 때문에 continue
                        continue
                    else:  # 줄이 바뀌면 buff 변경
                        buff = changeBuffer(buff)

                if buff == chessList[t][k]:
                    # print(buff, chessList[t][k], "(", t, k, ")")
                    cnt += 1
                    buff = changeBuffer(buff)
                else:
                    buff = chessList[t][k]
        if cnt < min_cnt:
            min_cnt = cnt

print(min_cnt)
