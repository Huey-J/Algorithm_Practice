# 주어진 식에 괄호를 적절히 쳐서 값을 최소로!
# -가 나오는 순간부터는 괄호를 활용해서 계속 -가 가능

cal = input()

temp_num = ''
flag = 0
total = 0
for temp in cal:
    if flag == 0 and temp == '-':
        flag = 1

    if temp.isnumeric():
        temp_num += temp
    else:
        if flag == 2:
            # print("-%d" % int(temp_num))
            total -= int(temp_num)
        elif flag == 1:
            flag = 2
            # print("+%d" % int(temp_num))
            total += int(temp_num)
        else:
            # print("+%d" % int(temp_num))
            total += int(temp_num)
        temp_num = ''

if flag == 2:
    # print("-%d" % int(temp_num))
    total -= int(temp_num)
else:
    # print("+%d" % int(temp_num))
    total += int(temp_num)
print(total)
