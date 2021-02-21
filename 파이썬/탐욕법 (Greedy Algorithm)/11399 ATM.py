n = int(input())
people = list(map(int, input().split()))
people.sort(reverse=True)

sum = 0
for i in range(len(people)):
    sum += people[i] * (i+1)

print(sum)
