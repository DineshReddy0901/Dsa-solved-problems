class Solution(object):
    def subArrayRanges(self, nums):
        sum = 0
        n = len(nums)
        
       
        for i in range(n-1):
            lar = nums[i]
            sma = nums[i]
            for j in range(i+1,n):
                lar = max(lar,nums[j])
                sma = min(sma,nums[j])
                sum += lar-sma
        return sum
        
        