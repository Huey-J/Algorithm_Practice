N = int(input())

member_list = []
for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append((age, name))

member_list.sort(key=lambda age: (age[0]))

for temp in member_list:
    print(temp[0], temp[1])
