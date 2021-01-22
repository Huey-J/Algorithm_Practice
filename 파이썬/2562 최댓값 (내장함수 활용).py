"""
    li = []
    for i in range(9):
        temp = int(input())
        li.append(temp)

    maxNumber = 0
    maxIndex = -1
    for i in range(len(li)):
        if li[i] > maxNumber:
            maxNumber = li[i]
            maxIndex = i

    print(maxNumber)
    print(maxIndex+1)
"""

# 모범 답안
num_list = []
for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)
