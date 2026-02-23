class Solution(object):
    def hasAllCodes(self, s, k):
        need = 1<<k
        got = [False]*need
        count =0
        num =0

        for i in range(len(s)):
            num = ((num<<1)) & (need-1) | int(s[i])
            if i>=k -1 and not got[num]:
                got[num] = True
                count +=1
                if count == need:
                    return True
        return False
        