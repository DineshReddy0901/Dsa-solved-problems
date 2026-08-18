class Solution(object):
    def largestInteger(self, nums, k):
        seen = {}
        left = 0
        for right in range(k-1,len(nums)):
            window = set()
            for i in range(left,right+1):
                window.add(nums[i])
            for num in window:
                seen[num] = seen.get(num, 0) + 1
            left+=1
        ans=-1
        for i in seen:
            if seen[i]==1:
                ans = max(ans,i)
        return ans

        
        
                 

            
           
           
                