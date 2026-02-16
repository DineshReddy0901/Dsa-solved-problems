class Solution(object):
    def maxSubArray(self, nums):
        result =nums[0]
        total =0
        for i in nums:
            if total<0:
                total=0
            total +=i
            result = max(result,total)
        return result
      
                