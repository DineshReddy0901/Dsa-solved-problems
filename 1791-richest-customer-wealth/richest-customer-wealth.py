class Solution(object):
    def maximumWealth(self, accounts):
        res = 0
        for i in accounts:
            res = max(res,sum(i))
        return res

        