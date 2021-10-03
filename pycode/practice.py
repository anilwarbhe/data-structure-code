class Solution:
    summ =0
    def valueEqualToIndex(self, arr, n):
        # for i, ele in enumerate(arr):
        #     if (ele == i+1):
        #         return ele
        foundele = 0
        for i in range(n):
            if arr[i]==i+1:
                return i+1
            
    # def nestedEvenSum(self, obj, summ):
    #     # key, val = obj.popitem()
    #     if obj != {}:
    #         if type(obj) == int:
    #             print(obj)
    #             if obj%2 ==0:
    #                 print(obj)
    #                 summ +=obj
    #                 print(summ)
    #         else:
    #             key, val = obj.popitem()
    #             # print(obj)
    #             # print(type(obj) == dict)
    #             # print(val)
    #             # print(type(val) == dict)
    #             self.nestedEvenSum(val, summ)
    #             self.nestedEvenSum(obj, summ)
    #             return val
    #     return summ

    # def nestedEvenSum(self, obj, summ):
    #     # key, val = obj.popitem()
    #     if obj != {}:
    #         if type(obj) == int:
    #             print(obj)
    #             if obj%2 ==0:
    #                 print(obj)
    #                 summ +=obj
    #                 print(summ)
    #                 # self.nestedEvenSum(val, summ)
    #         else:
    #             key, val = obj.popitem()
    #             # print(obj)
    #             # print(type(obj) == dict)
    #             # print(val)
    #             # print(type(val) == dict)
    #             self.nestedEvenSum(val, summ)
    #             self.nestedEvenSum(obj, summ)
    #             # return val
    #     # return summ

    # def nestedEvenSum(self, obj, summ):
    #     # key, val = obj.popitem()
    #     # print(obj)
    #     if obj != {}:
    #         if type(obj) == int:
    #             # print(obj)
    #             if obj%2 ==0:
    #                 # print(obj)
    #                 summ +=obj
    #                 print('top:',summ)
    #             return summ
    #                 # self.nestedEvenSum(val, summ)
    #         else:
    #             key, val = obj.popitem()
    #             # print(obj)
    #             # print(type(obj) == dict)
    #             # print(val)
    #             # print(type(val) == dict)
    #             print('val', val)
    #             print(val)
    #             print('obj', obj)
    #             if type(obj) == int and val%2 ==0:
    #                 summ = summ + val
    #                 print('summ:', summ)
    #             self.nestedEvenSum(val, summ)
    #             self.nestedEvenSum(obj, summ)
    #             # return val
    #     return summ

    # def nestedEvenSum(self, obj, summ):
    #     # key, val = obj.popitem()
    #     # print(obj)
        
    #     if obj == {}:
    #         return self.summ
    #     else:
    #         if type(obj) == int and obj%2 ==0:
    #             self.summ = self.summ + obj
    #             print('summ:', self.summ)
    #         else:
    #             if type(obj) != int:
    #                 key, val = obj.popitem()
    #                 print('val', val)
    #                 print(val)
    #                 print('obj', obj)            
    #                 self.nestedEvenSum(val, self.summ)
    #                 self.nestedEvenSum(obj, self.summ)
    #     print('summmm', self.summ)
    #     return self.summ    

    # def nestedEvenSum(self, obj, summ):       
    #     if obj != {}:
    #         if type(obj) == int: 
    #             if obj%2 ==0:
    #                 self.summ = self.summ + obj
    #                 print('summ:', self.summ)
    #         else:
    #             key, val = obj.popitem()
    #             print('val', val)
    #             print(val)
    #             print('obj', obj)            
    #             self.nestedEvenSum(val, self.summ)
    #             self.nestedEvenSum(obj, self.summ)
    #     print('summmm', self.summ)
    #     return self.summ    

    # def nestedEvenSum(self, obj, summ):       
    #     if obj != {}:
    #         if type(obj) == int: 
    #             if obj%2 ==0:
    #                 summ = summ + obj
    #                 print('summ:', summ)
    #             return summ
    #         elif type(obj) == str or type(obj)==bool:
    #             return summ
    #         else:
    #             key, val = obj.popitem()       
    #             return self.nestedEvenSum(val, summ) + self.nestedEvenSum(obj, summ)
    #     else:   
    #         print('summmm', summ)
    #         return summ    

    # def nestedEvenSum(self, obj, summ):       
    #     if obj != {}:
    #         if type(obj) == int: 
    #             if obj%2 ==0:
    #                 summ = summ + obj
    #                 print('summ:', summ)
    #             return summ
    #         elif type(obj) == str or type(obj)==bool:
    #             return summ
    #         else:
    #             key, val = obj.popitem()       
    #             return self.nestedEvenSum(val, summ) + self.nestedEvenSum(obj, summ)
    #     return summ    

    def nestedEvenSum(self, obj, summ):       
        if bool(obj) and type(obj) != str and type(obj)!=bool and type(obj)!=int and obj !={} :
            key, val = obj.popitem()       
            return self.nestedEvenSum(val, summ) + self.nestedEvenSum(obj, summ)
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
print("Solution: ", sol.nestedEvenSum(mydic, 0))