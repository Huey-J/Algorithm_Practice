N = int(input())
for i in range(N):
    str = input()

    cnt = 0  # '('의 개수 - ')'의 갯수

    for j in range(len(str)):
        if str[j] == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            print("NO")
            break

    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
