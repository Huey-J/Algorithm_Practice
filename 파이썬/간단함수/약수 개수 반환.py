def count_divisors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


print(count_divisors(1))
print(count_divisors(2))
print(count_divisors(8))
print(count_divisors(25))
print(count_divisors(100))
