from collections import Counter

def solution(str1, str2):
    # 대소문자 구분X
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 특수기호 뺀 문자 쌍 추출
    str1_lst, str2_lst = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_lst.append(str1[i] + str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            str2_lst.append(str2[j] + str2[j+1])
    
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())        # 교집합
    union = list((Counter1 | Counter2).elements())        # 합집합

    print(list((Counter1 & Counter2).elements()))
    print(list((Counter1 & Counter2)))

    # 반환 (int : 내림)
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)



# from collections import Counter

# def solution(str1, str2):
#     # 대소문자 구분X
#     str1 = str1.lower()
#     str2 = str2.lower()

#     # 특수기호 뺀 문자 쌍 추출
#     str1_list, str2_list = [], []
#     for i in range(len(str1) - 1):
#         if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z':
#             str1_list.append(str1[i] + str1[i+1])
#     for i in range(len(str2) - 1):
#         if 'a' <= str2[i] <= 'z' and 'a' <= str2[i+1] <= 'z':
#             str2_list.append(str2[i] + str2[i+1])

#     print(str1_list, str2_list)

#     # 0, 0일 경우 1 반환
#     if len(str1_list) == 0 and len(str2_list) == 0:
#         return 1 * 65536
    
#     minius, maximum = 0, 0
#     for i in range(min(len(str1_list), len(str2_list))):
#         if str1_list[i] == str2_list[i]:
#             minius += 1

#     # maximum = max(len(str1_list), len(str2_list))
#     # print(list(Counter(str1_list+str2_list)))
#     maximum = len(list(Counter(str1_list+str2_list)))

#     print(minius, maximum)
#     if maximum == 0 or minius == 0:
#         return 1 * 65536
#     return int(minius / maximum * 65536)


print(solution("FRANCE", "french"))