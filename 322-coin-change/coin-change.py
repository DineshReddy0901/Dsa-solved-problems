class Solution(object):
    def coinChange(self, coins, amount):
        # if amount is 0:
        #     return 0
        # sorted_coins = sorted(coins)
        # i = 0
        # j = len(sorted_coins)-1
        # f = sorted_coins[0]
        # while i<len(sorted_coins) and j<(sorted_coins):
        #     if f+sorted_coins[i]+sorted_coins[j]<amount:
        #         i +=1    
        #     elif f+sorted_coins[i]+sorted_coins[j]>amount:
        #         j-=1
        #     elif f + sorted_coins[i]+ sorted_coins[j]==amount:
        #         return 3
        #     else:
        


        if amount == 0:
            return 0

        visited = set()
        q = deque([(amount, 0)])  # (remaining, steps)

        while q:
            rem, steps = q.popleft()

            for coin in coins:
                nxt = rem - coin
                if nxt == 0:
                    return steps + 1
                if nxt > 0 and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, steps + 1))

        return -1