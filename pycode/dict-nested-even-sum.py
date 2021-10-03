#   Created by Anil Dada Warbhe
#   Copyright ©  All rights reserved.

# nestedEvenSum Solution
class Solution:
    def nestedEvenSumV1(self, obj, summ):       
        if obj != {}:
            if type(obj) == int: 
                if obj%2 ==0:
                    summ = summ + obj
                    print('summ:', summ)
                return summ
            elif type(obj) == str or type(obj)==bool:
                return summ
            else:
                key, val = obj.popitem()       
                return self.nestedEvenSumV1(val, summ) + self.nestedEvenSumV1(obj, summ)
        return summ    

    def nestedEvenSumV2(self, obj, summ):       
        if bool(obj) and type(obj) != str and type(obj)!=bool and type(obj)!=int and obj !={} :
            key, val = obj.popitem()       
            return self.nestedEvenSumV2(val, summ) + self.nestedEvenSumV2(obj, summ)
        else:
            if type(obj)==int:
                if obj%2 ==0:
                    summ = summ + obj
            return summ

sol = Solution()
# print(sol.valueEqualToIndex([15, 2, 45, 12, 7],5))
# mydic = {"aa":1, "ab":2}
# mydic = {"a":{"aa":1, "ab":2}}
# mydic = {"x": 3, "a":{"aa":1, "ab":2}}
# mydic = {"a":{"aa":1, "ab":2}, "b":{"aaa":1, "aab":2, "aac":3}}
mydic = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}
# mydic = {
#   "outer": 2,
#   "obj": {
#     "inner": 2,
#     "otherObj": {
#       "superInner": 2,
#       "notANumber": True,
#       "alsoNotANumber": "yup"
#     }
#   }
# }
# print("Val:", sol.nestedEvenSum(mydic, 0))
# print("Solution V1: ", sol.nestedEvenSumV1(mydic, 0))
print("Solution V2: ", sol.nestedEvenSumV2(mydic, 0))