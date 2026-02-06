class Solution(object):
    def findKthLargest(self, nums, k):
        # nums_sorted = sorted(nums)
        # index = len(nums) - k
        # return nums_sorted[index]

        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
            

        



