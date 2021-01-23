for i in range(int(input())):
    str = input()

    flag = 0
    score = 0
    for j in str:
        if j == 'O':
            flag += 1
            score += flag
        else :
            flag = 0

    print(score)
