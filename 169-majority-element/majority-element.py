class Solution(object):
    def majorityElement(self, nums):
        hash = {}
        result = 0
        highest =0
        for i in nums:
            hash[i] = 1+ hash.get(i,0)
            if hash[i] > highest:
                result = i
                highest = hash[i]
        return result
        