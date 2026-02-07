class Solution(object):
    def findRelativeRanks(self, score):
        N = len(score)
        heap = []

        for index, values in enumerate(score):
            heapq.heappush(heap, (-values, index))

        rank = [""] * N
        place = 1

        while heap:
            original_rank = heapq.heappop(heap)[1]

            if place == 1:
                rank[original_rank] = "Gold Medal"
            elif place == 2:
                rank[original_rank] = "Silver Medal"
            elif place == 3:
                rank[original_rank] = "Bronze Medal"
            else:
                rank[original_rank] = str(place)

            place += 1

        return rank
        # N = len(score)
        # heap = []
        # for index, values in enumerate(score):
        #     heapq.heappush(heap,(-values,index))
        #     rank = [""] * N
        #     place = 1
        #     while heap:
        #         original_rank = heapq.heappop(heap)[1]
        #         if place ==1:
        #             rank[original_rank] = "Gold Medal"
        #         elif place ==2:
        #             rank[original_rank] = "Silver Medal"
        #         elif place ==3:
        #             rank[original_rank] = "Bronze Medal"
        #         else:
        #             rank[original_rank]=str(place)
        #         place+=1
        #     return rank
                

            
            