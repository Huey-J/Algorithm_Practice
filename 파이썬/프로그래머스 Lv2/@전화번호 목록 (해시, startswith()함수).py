# # 내 답안 : 시간 초과
# def solution(phone_book):
#     length = len(phone_book)
#     for i in range(length):
#         for j in range(length):
#             if i == j:
#                 continue
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#     return True



# 모범 답안 : 해시 사용
def solution(phone_book):
    # 해시 맵 생성
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True



print(solution(	["12", "123", "1235", "567", "88"]))
