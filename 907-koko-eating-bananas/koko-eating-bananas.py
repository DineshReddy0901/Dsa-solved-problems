class Solution(object):
    def minEatingSpeed(self, piles, h):
        right = max(piles)
        left = 1

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for p in piles:
                hours += (p + mid - 1) // mid   # ceil(p / mid)

            if hours <= h:
                right = mid - 1   # try smaller speed
            else:
                left = mid + 1    # need bigger speed

        return left




        # n = len(piles)
        # if n == h:
        #     return piles[0]

        # speed = 1
        # max_speed = max(piles)

        # for i in range(n):
        #     if speed>=piles[i]:
        #         speed =i
        #     else:
        #         speed +=1
        # return speed       

        