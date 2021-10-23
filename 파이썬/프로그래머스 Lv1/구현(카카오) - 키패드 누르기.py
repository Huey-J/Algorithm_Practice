def solution(numbers, hand):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]
    leftHand = [3, 0]
    rightHand = [3, 2]

    result = ""
    for nowNumber in numbers:
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                if nowNumber == keypad[i][j]:
                    if j == 0:
                        result += "L"
                        leftHand = [i, j]
                    elif j == 1:
                        # 거리 비교
                        leftDistance = abs(i - leftHand[0]) + abs(j - leftHand[1])
                        rightDistance = abs(i - rightHand[0]) + abs(j - rightHand[1])

                        if leftDistance < rightDistance:
                            result += "L"
                            leftHand = [i, j]
                        elif leftDistance > rightDistance:
                            result += "R"
                            rightHand = [i, j]
                        else:
                            if hand == "left":
                                result += "L"
                                leftHand = [i, j]
                            else:
                                result += "R"
                                rightHand = [i, j]
                    else:
                        result += "R"
                        rightHand = [i, j]
    return result


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
