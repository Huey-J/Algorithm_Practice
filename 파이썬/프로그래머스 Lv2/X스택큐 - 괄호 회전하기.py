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


# 내 답안 (틀림)
# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         tmp = s[i:] + s[:i]

#         tmp_list = []
#         for c in tmp:
#             tmp_list.append(c)
        
#         now = []
#         for i in range(len(tmp_list)):
#             c = tmp_list.pop(0)
            
#             if len(now) == 0:
#                 now.append(c)
#             elif c == '[':
#                 if now[-1] == '{' or now[-1] == '(':
#                     break
#                 else:
#                     now.append('[')
#             elif c == '{':
#                 if now[-1] == '(':
#                     break
#                 else:
#                     now.append('{')
#             elif c == '(':
#                 now.append('(')
            
#             elif c == ']':
#                 if len(now) == 0:
#                     break
#                 if now[-1] == '[':
#                     now.pop(-1)
#                 else:
#                     break
#             elif c == '}':
#                 if len(now) == 0:
#                     break
#                 if now[-1] == '{':
#                     now.pop(-1)
#                 else:
#                     break
#             elif c == ')':
#                 if len(now) == 0:
#                     break
#                 if now[-1] == '(':
#                     now.pop(-1)
#                 else:
#                     break
#         else:
#             if len(now) == 0:
#                 answer += 1
#     return answer


# s = "(){{]]"
# print(solution(s))
