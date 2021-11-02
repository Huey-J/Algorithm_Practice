def solution(n):
    number3 = ""
    while n >= 3:
        number3 = str(n % 3) + number3
        n //= 3
    number3 = str(n) + number3

    answer = 0
    for i in range(0, len(number3)):
        answer += int(number3[i]) * 3**(i)
    return answer


print(solution(3))


# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환 후 반환
# int('1332', 4) : 126  (4진수인 1332를 10진수로 변환)


# pythonic한 코드 답안
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)     ################### int 내장 함수 사용
#     return answer