class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand)%groupSize != 0:
            return False
        freq = Counter(hand)
        for i in sorted(hand):
            if freq[i] == 0:
                continue
            for j in range(i,i+groupSize):
                if freq[j]==0:
                    return False
                freq[j]-=1
        return True


        
        