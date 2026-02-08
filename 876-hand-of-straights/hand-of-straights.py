class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand)% groupSize!=0:
            return False
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]

            for card in range(start,start+groupSize):
                if count[card]==0:
                    return False
                count[card]-=1
                # if count[card]==0:
                #     if card!= min_heap[0]:
                #         return False
            while min_heap and count[min_heap[0]]==0:
                heapq.heappop(min_heap)
        return True
                  

            #         else:
            #             heapq.heappop(min_heap)
            # return True





        