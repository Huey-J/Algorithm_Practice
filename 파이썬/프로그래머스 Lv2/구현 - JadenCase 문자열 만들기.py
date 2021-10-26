def solution(s):
    answer = ''
    str_list = s.split(' ')
    for str in str_list:
        if str != '':
            answer += str[0].upper() + str[1:].lower() + ' '
        else:
            answer += ' '
    return answer[:-1]


s = "3people 1 a v  C UnFOllo32wed Me"
print(solution(s))
