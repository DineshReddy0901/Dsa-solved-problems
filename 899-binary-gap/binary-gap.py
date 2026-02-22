class Solution(object):
    def binaryGap(self, n):
            set_bits = bin(n)[2:]
            prev =-1
            result =0
            
            
            for i in range(len(set_bits)):
                if  set_bits[i] =='1':
                    if prev!=-1:
                        result = max(result,i-prev)
                    prev =i
            return result
                    
               


                
        