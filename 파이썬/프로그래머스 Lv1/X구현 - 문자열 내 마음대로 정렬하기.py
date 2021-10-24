def solution(strings, n):
    str = []
    for i in strings:
        str.append(i[n]+i)       # n번째 문자를 앞에 붙임
    str.sort()
    return [i[1:] for i in str]


strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))
