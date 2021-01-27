x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

x_list = [x_1, x_2, x_3]
y_list = [y_1, y_2, y_3]

other_x = 0
other_y = 0
for i in x_list:
    if (x_list.count(i) == 1):
        other_x = i
for i in y_list:
    if (y_list.count(i) == 1):
        other_y = i

print(other_x, other_y)

# 더 깔끔한 소스
'''
x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1
        y = y_list[i]
print(x, y)
'''
