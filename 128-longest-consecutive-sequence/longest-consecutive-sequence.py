class Solution(object):
    def longestConsecutive(self, nums):
        longest_count = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current = num
                count = 1
                while current+1 in num_set:
                    current+=1
                    count+=1
                longest_count= max(longest_count,count)
        return longest_count       