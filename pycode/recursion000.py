import math

def factorial(num):
    assert num > 0, 'The number must be positive integer only'
    if num in [0, 1]:
        return 1
    else:
        return num * factorial(num-1)
# num = int(input("Enter the Number: "))
# fact = factorial(num)
# print(fact)


# def fibonacci(fn, sn, count):
#     # print(fn,sn,count)
#     if count > 0:
#         print(str(fn)+",")
#         return fibonacci(sn, fn+sn, count-1)


# num = int(input("Enter the Number: "))
# fibonacci(0, 1, num)

# def fibonacci(num):
#     if num in [0, 1]:
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)

# n = int(input("How many numbers in a Fibinacci sequence?: "))
# for num in range(n):
#     print(fibonacci(num))


# def fibonacci(fn, sn, count):
#     # print(fn,sn,count)
#     if count in [0, 1]:
#         print(fn)
#         return fn
#     else:
#         # print(str(fn)+",")
#         print(fn)
#         return fibonacci(sn, fn+sn, count-1)


# num = int(input("Enter the Number: "))
# fibonacci(0, 1, num)

class Solution:
    def isPowerOfTwo1(self, n: int) -> bool:
        retflag = False
        for i in range(n):
            if n == 2 ** i:
                retflag = True
        return retflag
    
    def isPowerOfTwo2(self, n: int) -> bool:
        return ((n!=0) and ( (n & (n-1)) == 0))

# num = int(input("Enter the Number: "))
# s = Solution()
# print(s.isPowerOfTwo(num))

print(math.ceil(5.1))
print(math.floor(5.1))

def isPowerOfTwo(n):
    return ((n!=0) and ( (n & (n-1)) == 0))

print(isPowerOfTwo(2))
print((3 | 2))