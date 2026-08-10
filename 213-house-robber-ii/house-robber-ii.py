class Solution(object):
    def rob(self,nums):
        n = len(nums)
        if n==1:
            return nums[0]
        ans1 = self.rob_range(nums[:n-1])
        ans2 = self.rob_range(nums[1:])

        return max(ans1,ans2)
        
    def rob_range(self, nums):
        prev1 = 0
        prev2 = 0
        for i in nums:
            curr = max(prev1,prev2+i)
            prev2 = prev1 
            prev1 = curr
        return prev1