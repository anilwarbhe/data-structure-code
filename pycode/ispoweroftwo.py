import math
# from collections import  List 
def log2(num):
    return (math.log10(num)/math.log10(2))

class IsPowerOfTwo:
    def isPowerOfTwoV1(self, n: int) ->bool:
        return (n!=0 and (n & (n-1) ==0))

    def isPowerOfTwoV2(self, n:int) ->bool:
        x = log2(n)
        return math.ceil(x) == math.floor(x)


# p = IsPowerOfTwo()
# nval =64
# print(p.isPowerOfTwoV1(nval))
# print(p.isPowerOfTwoV1(nval))
# x=8
# print(int(x>>1))
# print(int(x<<1))
# x>>=1
# print(x)

# print(f"{4 :b}")
# print(f"{4 :032b}")
# bnum = f"{4:032b}"
# print(bnum==f)
# print(int(bnum,2))

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

def HammingWeightV1(thirtytwobitbinaryno):
    # if int(thirtytwobitbinaryno,2) in [f"{0:032b}", f"{1:032b}"]:
    count = 0
    intval = int(thirtytwobitbinaryno, 2)
    while(intval!=0):
        if (intval & 1 ==1):
            count += 1
        intval >>= 1        
    return count

def HammingWeightV2(thirtytwobitbinaryno):
    return thirtytwobitbinaryno.count("1")

bnum = f"{7:032b}"
# print(HammingWeightV1(bnum))
# print(HammingWeightV2(bnum))

class Solution:
    def twoSum(self, nums, target):
        indxlst = []
        indxval = 1
        for no in nums:
            newnums = nums[indxval:len(nums)+1]
            for nextnum in newnums:
                # print(no, nextnum)
                if no + nextnum  == target:
                    print('appending')
                    indxlst.append(nums.index(no))
                    indxlst.append(newnums.index(nextnum)+indxval)
                    break;
            indxval+=1
        return indxlst

# s = Solution()
# print(s.twoSum([3,2,4],6))
# print(s.twoSum([2,7,11,15],9))
# print(s.twoSum([3,3],6))
# print(s.twoSum([11,15,3,3],6))
# print(s.twoSum([11,3,13,3],6))

# S = "ababaaaab"
# print(S.split('a'))
# print(S.split('ab'))
# print(S.split('aba'))
# print("@@@@@@@@@@@@@@@@@@@@@@@@")
# S = "aaaa"
# print(S.split('a'))
# print(S.split('aa'))
# print(S.split('aaa'))

def splitter(str):
    # for i in range(len(str)):
    substr = ''
    for i in str:
        substr +=i
        life = str.split(substr)
        if len(life) == len(str)+1:
            # print("The frequency of occurance of '%s' is %d" %(substr,len(str)))
            print("The frequency of occurance of '%s' is %d" %(substr,life.count('')-1))
            break
        elif(life[0]==life[-1]):
            if len(life) == life.count(''):
                print("The frequency of occurance of '%s' is %d" %(substr,life.count('')-1))
            else:
                print("The frequency of occurance of '%s' is %d" %(substr,life.count('')))
            break

# splitter("ababaaaab")
# splitter("abcdef")

# class Solution:
#     def maxFrequency(self, S):
#         # code here
#         frequency = 0
#         substr = ''
#         for i in S:
#             substr +=i
#             life = S.split(substr)
#             if len(life) == len(S)+1:
#                 frequency = life.count('')-1
#                 break
#             elif(life[0]==life[-1]):
#                 if len(life) == life.count(''):
#                     frequency = life.count('')-1
#                 else:
#                     frequency = life.count('')
#                 break
#         return frequency

# class Solution:
#     def maxFrequency(self, S):
#         # code here
#         frequency = 0
#         substr = ''
#         for i in S:
#             substr +=i
#             life = S.split(substr)
#             print(life)
#             if len(life) == life.count(''):
#                 frequency = life.count('')-1
#                 break
#             elif(life[0]==life[-1]):
#                 frequency = life.count('')
#                 break
#         return frequency

# sol = Solution()
# print(sol.maxFrequency("abacaba"))

class Solution:
    def maxFrequency(self, S):
        # code here
        frequency = 0
        substr = ''
        for i in S:
            substr +=i
            life = S.count(substr)
            print(life)
            if S.endswith(substr):
                print(substr)
                frequency = life
                break
        return frequency

sol = Solution()
# print(sol.maxFrequency("abacaba")) //Correcy output=4
print(sol.maxFrequency("abcdef"))

# class Solution:
#     def maxFrequency(self, s):
#         n=len(s)
#         for i in range(n):
#             x=s[:i+1]
#             if s.endswith(x):
#                 return s.count(x)
#         return 1   