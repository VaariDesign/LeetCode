
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       nums_d = {};
       for i, n in enumerate(nums):
           if((target - n) in nums_dict.keys()):
               return [nums_dict[target - n], i]
           nums_d[n] = i
