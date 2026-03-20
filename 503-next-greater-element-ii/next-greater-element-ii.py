class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack= []
        res = [-1]*n
        for i in range(2*n -1,-1,-1):
            while stack and nums[stack[-1]] <=nums[i%n]:
                stack.pop()
            if stack:
                res[i%n] = nums[stack[-1]]
            stack.append(i%n)
        return res