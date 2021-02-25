def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        tmp = n % 3
        if tmp == 0:
            tmp_str = '1'
        elif tmp == 1:
            tmp_str = '2'
        else:
            tmp_str = '4'
        answer = tmp_str + answer
        n //= 3
    return answer


print(solution(2))
