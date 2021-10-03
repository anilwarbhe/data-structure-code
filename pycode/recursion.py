class Recursion:
    def factorial(self, num):
        if num in [0, 1]:
            return 1
        else:
            return num * self.factorial(num-1)
    
    def arestob(self, a, b):
        if b == 1:
            return a
        else:
            return a * self.arestob(a, b-1)
    
    # def fibonacci(self, num):
    #     if num in [0,1]:
    #         return num
    #     else:
    #         return self.fibonacci(num-1)+self.fibonacci(num-2)

    def fibonacci(self, num):
        if num in [0,1]:
            return num
        else:
            return self.fibonacci(num-1)+self.fibonacci(num-2)
    
    def faconacci_sequence(self, fn, sn, count):
        if count >= 0:
            print('count',count)
            print(fn)
            return self.faconacci_sequence(sn, fn+sn, count-1)

    def addallnumsinadigit(self, num):
        if num//10 == 0:
            return num%10
        else:
            return num%10+self.addallnumsinadigit(num//10)

    def GCD(self, num1, num2):
        if num1%num2 == 0:
            return num2
        else:
            return self.GCD(num2, num1%num2)
        
    def decimal2binary(self, num):
        if num==0:
            return 0
        else:
            return (num%2)+10 * self.decimal2binary(num//2)
             
    def isPalindrome(self, strng):
        if len(strng) == 0:
            return True
        if strng[0] != strng[len(strng)-1]:
            return False
        print(strng[1:-1])
        return self.isPalindrome(strng[1:-1])

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()

        for i, num in enumerate(nums):
            print(hash_table)
            try:
                print(i)
                hash_table[target - num]
                return [hash_table[target - num], i]
            except KeyError:
                print('error')
                hash_table[num] = i

def convertFive(n):
    if n/10 == 0:
        return 0
    else:
        if n%10==0:
            return convertFive(n//10)*10+5
        else:
            return convertFive(n//10)*10+(n%10)
r = Recursion()
# print(r.factorial(3))
# print(r.arestob(2, 2))
# print(r.fibonacci(6))
# r.faconacci_sequence(0, 1, 7)
# print(r.addallnumsinadigit(12345))
# print(r.GCD(48,18))
# print(r.decimal2binary(7))
# print(r.isPalindrome('tacocat'))
# print(r.twoSum([2,7,11,15],17))
print(convertFive(12003))
# print(1234/10)
