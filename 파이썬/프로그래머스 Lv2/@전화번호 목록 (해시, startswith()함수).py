#### 내 답안 1
# def solution(phone_book):
#     for number in phone_book:
#         number_stack = []  # 순서가 거꾸로 된 stack
#         tmp = int(number)
#         while tmp > 0:
#             number_stack.append((tmp % 10))
#             tmp //= 10
#
#         # 접두사인지 체크
#         for other_number in phone_book:
#             if other_number == number:
#                 continue
#             for i in range(0, len(str(other_number))):
#                 a = number_stack[len(number_stack) - i - 1]
#                 if int(str(other_number)[i]) != a:
#                     break
#             else:
#                 return False
#     return True

#### 내 답안 2
def solution(phone_book):
    for A in phone_book:
        for B in phone_book:
            if A == B:
                continue
            if B.startswith(A):
                return False
    return True


print(solution(["123", "456", '789']))

#### 모범답안
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1): # startswith 함수로 체크
#             return False
#     return True
