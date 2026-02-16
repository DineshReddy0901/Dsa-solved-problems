class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        counts = Counter(nums)
        return max(counts,key=counts.get)
        
        