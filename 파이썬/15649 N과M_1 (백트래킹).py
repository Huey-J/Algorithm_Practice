N, M = map(int, input().split())

check = [False] * (N + 1)
num_list = [0] * M


def printing(index):
    if index == M:
        for i in range(M):
            print(num_list[i], end=" ")
        print()
        return

    for i in range(1, N + 1):
        if check[i]:
            continue
        check[i] = True
        num_list[index] = i
        printing(index + 1)
        check[i] = False


printing(0)
