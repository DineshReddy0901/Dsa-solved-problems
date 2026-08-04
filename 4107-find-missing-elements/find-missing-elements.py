class Solution(object):
    def findMissingElements(self, nums):
        nums.sort()
        res = []
        curr = nums[0]
        for i in range(len(nums)):
            while curr<nums[i]:
                res.append(curr)
                curr +=1
            curr = nums[i]+1
        return res
                
        
        