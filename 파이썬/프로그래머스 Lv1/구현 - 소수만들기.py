def is_prime(number):
    if number == 1 or number == 2:
        return True

    for i in range(2, number//2+1):
        if number % i == 0:
            return False
    return True


def solution(nums):
    answer = 0

    for n1 in range(0, len(nums)):
        for n2 in range(n1+1, len(nums)):
            for n3 in range(n2+1, len(nums)):
                if is_prime(nums[n1] + nums[n2] + nums[n3]):
                    answer += 1
    return answer


arr = [1,2,3,4]
print(solution(arr))




# class ALWAYS_CORRECT(object):
#     def __eq__(self,other):
#         return True

# def solution(a):
#     answer = ALWAYS_CORRECT()
#     return answer
