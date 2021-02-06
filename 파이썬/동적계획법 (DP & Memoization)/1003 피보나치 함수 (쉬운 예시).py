'''
ctn = [0, 0]


def fibonacci(n):
    if n == 0:
        ctn[0] += 1
        return 0
    elif n == 1:
        ctn[1] += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


T = int(input())
for _ in range(T):
    input_num = int(input())
    fibonacci(input_num)
    print(ctn[0], ctn[1])
    ctn = [0, 0]
'''

# 위 코드는 재귀로 품 / 시간초과

cnt0 = [1, 0]
cnt1 = [0, 1]

# 나열해 보면 0과 1의 갯수도 피보나치수열이므로 미리 만들어 놓기 (N<=40이라는 제한이 있기 때문에 가능)
for i in range(2, 41):
    cnt0.append(cnt0[i - 1] + cnt0[i - 2])
    cnt1.append(cnt1[i - 1] + cnt1[i - 2])

for _ in range(int(input())):
    n = int(input())
    print(cnt0[n], cnt1[n])
