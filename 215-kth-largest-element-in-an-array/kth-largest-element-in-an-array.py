class Solution(object):
    def findKthLargest(self, nums, k):
        nums_sorted = sorted(nums)
        index = len(nums) - k
        return nums_sorted[index]
        



