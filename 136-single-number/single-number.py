class Solution(object):
    def singleNumber(self, nums):
        counted_nums = Counter(nums)
        return min(counted_nums,key = counted_nums.get)
        
        