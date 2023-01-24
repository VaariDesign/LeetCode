class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ls = len(nums)
        if(ls < 3):
            return []
        nums = sorted(nums)
        resus = sum(nums[0:3])
        for i in range(ls - 2):
            j = i + 1
            m = ls - 1

            while(j < m):
                temp = nums[i] + nums[j] + nums[m]
                v = temp - target

                if(abs(v) < abs(resus - target)):
                    resus = temp

                if(v == 0):
                    return target
                elif(v > 0):
                    m -= 1
                else:
                    j += 1

        return resus
