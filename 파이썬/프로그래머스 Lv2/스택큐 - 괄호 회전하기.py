def solution(s):
    answer = 0
    for _ in s:
        # print("START", s)
        str_stack = []

        for i in range(len(s)):
            str_stack.append(s[i])

            # 맨 뒤가 짝이 맞는지 확인
            while len(str_stack) > 1:
                if str_stack[-2] == '(' and str_stack[-1] == ')' or str_stack[-2] == '{' and str_stack[-1] == '}' or str_stack[-2] == '[' and str_stack[-1] == ']': 
                    # print("@@@", str_stack)
                    str_stack.pop()
                    str_stack.pop()     # 맞으면 pop
                else:
                    break
        # print("END",str_stack)

        # 스택이 비어있으면 완벽한 괄호 문자
        if len(str_stack) == 0:
            answer += 1

        # 회전
        s = s[1:] + s[0]
        # print()
    
    return answer


print("return is ", solution("[]{}"))


# 내 답안
# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         tmp_str = s
#         print("STRAT", tmp_str)
#         while True:
#             if len(tmp_str) < 1:
#                 break
            
#             # 마지막 글자 추출
#             last_char = tmp_str[-1]
#             tmp_str = tmp_str[:-1]

#             # 마지막 글자가 시작 괄호면 제외
#             if last_char == '(' or last_char == '{' or last_char == '[':
#                 break
            
#             j = len(tmp_str) - 1
#             while j >= 0:
#                 if last_char == ')' and tmp_str[j] == '(' or last_char == '}' and tmp_str[j] == '{' or last_char == ']' and tmp_str[j] == '[':
#                     tmp_str = tmp_str[:j] + tmp_str[j+1:]
#                     j -= 1
#                     break
#                 j -= 1
#             else:   # 끝까지 last_char와 짝이 맞는 괄호를 찾지 못하면 제외
#                 break


#         print(">>>>>>>>>>>>> 남은거", tmp_str)
#         if len(tmp_str) == 0:
#             answer += 1

#         # 회전
#         s = s[1:] + s[0]
#     return answer

































# 모범 답안
# from collections import deque
# def check(s):
#     stack = []
#     for c in s:
#         if c == '(' or c == '{' or c == '[':
#             stack.append(c)
#         else:
#             if not stack:
#                 return False
#             x = stack.pop()
#             if c == ')' and x != '(':
#                 return False
#             elif c == ')' and x != '(':
#                 return False
#             elif c == '}' and x != '{':
#                 return False
#     return len(stack) == 0
# def solution(ip):
#     ip = deque(ip)
#     answer = 0
#     for x in range(len(ip)):
#         ip.rotate(-1)
#         if check(ip):
#             answer += 1
#     return answer

