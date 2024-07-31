PROGRAM: TWO SUM
class Solution:
    def twoSum(self,nums,targets):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==targets:
                    return [i,j]
