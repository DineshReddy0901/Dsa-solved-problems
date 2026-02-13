class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        if k==n:
            return sum(cardPoints)
        total_sum = sum(cardPoints)
        sub_array = n-k
        sub_array_sum = sum(cardPoints[:sub_array])
        min_sub_array_sum = sub_array_sum
        left =0 
        for right in range(sub_array,n):
            sub_array_sum += cardPoints[right] 
            sub_array_sum -= cardPoints[left]
            left+=1
            min_sub_array_sum = min(min_sub_array_sum,sub_array_sum)
        return total_sum - min_sub_array_sum


    
            
            


        
        