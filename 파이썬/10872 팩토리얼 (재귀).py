def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)


N = int(input())
print(factorial(N))
