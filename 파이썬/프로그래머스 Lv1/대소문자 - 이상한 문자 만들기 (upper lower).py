def solution(s):
    answer = ""
    s_list = list(s.split(' '))
    
    for str in s_list:
        for i in range(len(str)):
            if i % 2 == 0:
                answer += str[i].upper()
            else:
                answer += str[i].lower()
        answer += ' '

    return answer[:-1]


s = "try hello world"
print(solution(s))