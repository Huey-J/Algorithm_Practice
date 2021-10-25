def solution(n, words):
    tmp = []
    wrongIndex = []
    for i in range(len(words) - 1):
        # 끝말잇기 틀린 사람
        if words[i][-1] != words[i+1][0]:
            wrongIndex.append(i + 1)
        tmp.append((words[i], i))
    tmp.append((words[-1], len(words)-1))

    # 중복된 단어가 있는지 확인
    tmp2 = sorted(tmp, key=lambda x:x[0])
    for i in range(len(tmp2)):
        for j in range(i+1, len(tmp2)):
            if tmp2[i][0] == tmp2[j][0]:
                if tmp2[i][1] < tmp2[j][1]:
                    wrongIndex.append(tmp2[j][1])
                else:
                    wrongIndex.append(tmp2[i][1])
    
    wrongIndex = list(set(wrongIndex))
    if len(wrongIndex) != 0:
        return [min(wrongIndex)%n+1, min(wrongIndex)//n+1]
    else:
        return [0, 0]


n, words = 2, ["tank", "king", "tank", "tank", "tank", "tank"]
print(solution(n, words))
