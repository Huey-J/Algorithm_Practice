def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)  # a->c로 원판 이동
    else:
        hanoi(n - 1, a, c, b)  # a->b로 원판 이동(시작 기둥에서 중간 기둥으로)
        print(a, c)
        hanoi(n - 1, b, a, c)  # b->c로 원판 이동(중간 기둥에서 마지막 기둥으로)


n = int(input())
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)
