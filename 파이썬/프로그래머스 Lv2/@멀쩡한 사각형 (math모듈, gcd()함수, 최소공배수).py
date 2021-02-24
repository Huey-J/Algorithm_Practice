def solution(w, h):
    from math import gcd  # 최대공약수 함수
    return w * h - (h + w - gcd(w, h))


print(solution(4, 1))
