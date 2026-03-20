class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1] 

    
        
        