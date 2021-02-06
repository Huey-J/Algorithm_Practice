'''
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        memo[(20, 20, 20)] = w(20, 20, 20)  # { (a,b,c) : 값 } 구조인 딕셔너리
        return memo[(20, 20, 20)]
        
    if (a, b, c) in memo.keys():  # 메모에 있다면 바로 반환
        return memo[(a, b, c)]

    elif a < b < c:
        memo[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memo[(a, b, c)]

    else:
        memo[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return memo[(a, b, c)]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    memo = dict()
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
'''


# 위 코드는 시간오류

def w(dp, a, b, c):
    if a <= 0 or b <= 0 or c <= 0:  # 하나라도 0보다 같거나 작으면 1반환
        return 1
    elif a > 20 or b > 20 or c > 20:  # 하나라도 20보다 크면 전부 20으로 set
        return w(dp, 20, 20, 20)

    if dp[a][b][c] != 0:  # 아직 저장되지 않은 값은 계산
        return dp[a][b][c]

    # 계산한 값을 dp에 저장
    if a < b and b < c:
        dp[a][b][c] = w(dp, a, b, c - 1) + w(dp, a, b - 1, c - 1) - w(dp, a, b - 1, c)
    else:
        dp[a][b][c] = w(dp, a - 1, b, c) + w(dp, a - 1, b - 1, c) + w(dp, a - 1, b, c - 1) - w(dp, a - 1, b - 1, c - 1)

    # 해당 dp값 반환
    return dp[a][b][c]


def main():
    dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]  # 범위만큼 선언
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break
        print("w(%d, %d, %d) = %d" % (a, b, c, w(dp, a, b, c)))


if __name__ == "__main__":
    main()
