class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count = {0:1}
        count = 0
        sum_count = 0

        for num in nums:
            sum_count+=num

            if sum_count -k in prefix_count:
                count+= prefix_count[sum_count-k]
            prefix_count[sum_count] = prefix_count.get(sum_count,0) + 1
        return count
        