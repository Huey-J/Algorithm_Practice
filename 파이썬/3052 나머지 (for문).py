num_list = []
for i in range(10):
    temp = int(input())
    num_list.append(temp % 42)

num_set = set(num_list)
print(len(num_set))
