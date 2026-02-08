class Solution(object):
    def findContentChildren(self, g, s):
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        

        i =0
        j=0
        count =0
        while i<len(sorted_s) and j<len(g):
            if sorted_s[i]>=sorted_g[j]:
                j+=1
                i+=1
                count +=1
            else:
                i+=1
        return count


        
        