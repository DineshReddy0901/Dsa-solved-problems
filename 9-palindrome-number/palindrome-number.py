class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        reversed =0
        number =x
        while number!=0:
            reversed = reversed*10+number%10
            number  = number//10
        return reversed == x
  
        

            
    
        
        
        