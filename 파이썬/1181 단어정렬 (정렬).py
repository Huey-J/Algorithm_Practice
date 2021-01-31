N = int(input())
strList = []
for _ in range(N):
    input_word = input()
    strList.append(input_word)

strList = list(set(strList))    # 중복 제거
sortedList = []                 # 빈 리스트 생성

for temp in strList:            # 문자 길이가 포함된 리스트 생성
    sortedList.append([len(temp), temp])

sortedList.sort()
for temp in sortedList:
    print(temp[1])
