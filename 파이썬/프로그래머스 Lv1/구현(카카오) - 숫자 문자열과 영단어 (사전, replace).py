# # 모범답안 : dictionary, replace 사용
# def solution(s):
#     num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
#     for key, value in num_dic.items():
#         s = s.replace(key, value)
#     return int(s)


def solution(s):
    answer = ""
    number_strings = [(0, "zero"), (1, "one"),
        (2,	"two"), (3,	"three"),
        (4,	"four"), (5,	"five"),
        (6,	"six"), (7,	"seven"),
        (8,	"eight"), (9,	"nine"),
    ]

    i = 0
    while 0 < len(s):
        # 숫자일 경우
        if s[i] == '0' or s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9':
            answer += s[i]
            s = s[i+1:]
        # 문자일 경우
        else:
            for number_string in number_strings:
                if s.find(number_string[1]) == 0:
                    answer += str(number_string[0])
                    s = s[len(number_string[1]):]
                    break
        # print(answer, s)
    return int(answer)


print(solution("23four5six7"))
